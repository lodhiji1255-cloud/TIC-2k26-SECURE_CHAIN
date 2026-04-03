from flask import Flask, request, jsonify, send_from_directory, g
from flask_cors import CORS
from web3 import Web3
from models import Voter, Admin, SessionLocal
from face_utils import encode_face, compare_faces, hash_encoding
import numpy as np
import os, json, base64, cv2, bcrypt, jwt, datetime
from functools import wraps

from config.secret import (
    JWT_SECRET,
    ADMIN_PRIVATE_KEY,
    ADMIN_ACCOUNT,
    CONTRACT_ADDRESS,
    ABI_PATH,
    RPC_URL,
)

BASE_DIR = os.path.dirname(os.path.abspath(_file_))
FRONTEND_PATH = os.path.join(BASE_DIR, "../frontend")   
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(_name_, static_folder=FRONTEND_PATH, static_url_path="")
CORS(app)

# ---------------- Blockchain Setup ----------------
w3 = Web3(Web3.HTTPProvider(RPC_URL))
print("Blockchain Connected:", w3.is_connected())

with open(ABI_PATH, "r", encoding="utf-8") as f:
    contract_json = json.load(f)
abi = contract_json if isinstance(contract_json, list) else contract_json.get("abi")

contract = w3.eth.contract(
    address=Web3.to_checksum_address(CONTRACT_ADDRESS),
    abi=abi,
)

# ---------------- Helpers ----------------
def get_bytes(val):
    if isinstance(val, (bytes, bytearray, memoryview)):
        return bytes(val)
    return bytes(val) if val is not None else b""

def save_image_b64(data_url, dest):
    """
    data_url: "data:image/jpeg;base64,...." OR pure base64 string
    return: numpy BGR image
    """
    if "," in data_url:
        _, encoded = data_url.split(",", 1)
    else:
        encoded = data_url

    img_bytes = base64.b64decode(encoded)
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Invalid Base64 image")

    cv2.imwrite(dest, img)
    return img


def safe_delete(path):
    try:
        if os.path.exists(path):
            os.remove(path)
    except:
        pass


def send_contract_tx(fn, *args, gas=350000):
    """
    Helper to send tx & catch revert messages nicely.
    Returns (tx_hash_str, error_str)
    """
    try:
        nonce = w3.eth.get_transaction_count(ADMIN_ACCOUNT)
        tx = fn(*args).build_transaction(
            {
                "from": ADMIN_ACCOUNT,
                "nonce": nonce,
                "gas": gas,
                "gasPrice": w3.to_wei("1", "gwei"),
            }
        )
        signed = w3.eth.account.sign_transaction(tx, private_key=ADMIN_PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
        
        return tx_hash.hex(), None
    except ValueError as e:
        err = e.args[0]
        reason = ""
        if isinstance(err, dict):
            # Ganache style
            reason = (
                err.get("data", {}).get("reason")
                or err.get("data", {}).get("message")
                or err.get("message", "")
            )
        else:
            reason = str(err)
        return None, reason or "Blockchain error"
    except Exception as e:
        return None, str(e)
