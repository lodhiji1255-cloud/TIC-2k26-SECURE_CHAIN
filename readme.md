🗳️ Decentralized Voting System with Facial Authentication

A secure, tamper-proof blockchain-based voting platform that authenticates voters using live facial recognition and permanently records votes on the Ethereum blockchain.

This system is designed to ensure fair, transparent, and decentralized elections with strong identity verification.

✅ Key Guarantees

✔ One person = one vote
✔ Live camera authentication (no image upload allowed)
✔ Immutable vote storage on blockchain
✔ Secure admin panel with face-based login
✔ Fully decentralized and transparent vote counting

🚀 Features
🔒 1. Admin Authentication (3-Level Security)

Username verification

Password authentication (bcrypt hashed)

Live face verification via camera

🧑‍💼 2. Admin Dashboard

Add candidates (stored on blockchain)

Register voters using live face capture

View all registered voters

Secure access using JWT-based session control

🧑‍🎓 3. Voter Registration

Enrollment number & full name

Live camera capture only

Face encoding generation

Secure storage:

Full face embedding → MySQL

SHA-256 face hash → Blockchain

🗳️ 4. Cast Vote

Enrollment number based identification

Live face verification

Duplicate vote prevention

Vote recorded permanently on blockchain

📊 5. Live Results

Results fetched directly from Smart Contract

No manual intervention

Real-time, tamper-proof counting

🛠 Tech Stack
🔙 Backend

Python (Flask)

OpenCV

MediaPipe / face_recognition

NumPy

SQLAlchemy + MySQL

bcrypt

PyJWT

Web3.py

🌐 Frontend

HTML5

CSS3

JavaScript

Webcam-based face capture

⛓ Blockchain

Solidity Smart Contract

Ethereum

Ganache / Hardhat / Infura

📂 Project Structure
project/
│
├── backend/
│   ├── app.py
│   ├── create_admin.py
│   ├── face_utils.py
│   ├── models.py
│   ├── managedelection.sol
│   ├── config/
│   │   └── secret.py
│   ├── uploads/
│   └── venv310/              # Python Virtual Environment
│
└── frontend/
    ├── index.html
    ├── admin_login.html
    ├── admin.html
    ├── voter.html
    ├── candidate.html
    ├── results.html
    └── style.css

⚙ Installation & Setup
1️⃣ Install Requirements

Python 3.10 recommended

pip install -r requirements.txt


⚠️ dlib is platform-dependent.
Install separately if required (Windows wheel / Linux build).

2️⃣ Configure MySQL
CREATE DATABASE decentralised_voting;


Update credentials in:

backend/models.py
backend/config/secret.py

3️⃣ Configure Blockchain (Important)

Edit backend/config/secret.py:

RPC_URL = "http://127.0.0.1:7545"
CONTRACT_ADDRESS = "0xYourContractAddress"
ADMIN_PRIVATE_KEY = "your-private-key"
ADMIN_ACCOUNT = "0xAdminAccount"


Deploy managedelection.sol and paste the contract address.

4️⃣ Run Server
cd backend
python app.py


Server runs at:

http://127.0.0.1:5000

👨‍💼 Create Admin (First Time Only)
python create_admin.py


Process:

Enter username

Enter password

Camera opens → capture face

Admin stored securely (hashed password + face encoding)

🔐 Admin Login Flow

Visit:

/admin


Enter username & password

Live face verification

Redirect to secure admin dashboard

🧑‍🎓 Register a Voter

Admin login required

Open:

/voter


Enter enrollment number & name

Capture live face

Voter stored in DB + blockchain hash

🗳 Cast Vote

Visit home page /

Enter enrollment number

Capture live face

Select candidate

Vote stored permanently on blockchain

📊 View Election Results

Visit:

/results


Displays real-time results directly from smart contract.

🔍 Face Recognition Pipeline
Live Camera
   ↓
Face Detection
   ↓
Face Encoding (128-D Vector)
   ↓
Face Comparison
   ↓
SHA-256 Hash
   ↓
Blockchain Vote Record

🛡 Security Highlights
Protection	Status
Duplicate vote prevention	✔
Live face verification	✔
Admin 3-layer authentication	✔
Blockchain immutability	✔
No centralized manipulation	✔
📜 License

MIT License
(Free to modify for academic and educational use)

👤 Authors

Team Secure Chain

Sourabh Lodhi

Abhishek Singh

Ankit Chaurasiya

Harshit Garg

Kashish Gour

⭐ Final Note

This project demonstrates a real-world application of blockchain + biometric security and is suitable for:

Academic projects

Research demos

Security & blockchain showcases