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