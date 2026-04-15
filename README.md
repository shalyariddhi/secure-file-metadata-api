# Secure File Metadata API 🛡️

A high-performance FastAPI backend designed to process file uploads with a focus on **Data Integrity** and **Security**. This project implements cryptographic hashing to ensure that files stored and tracked remain untampered.

## 🚀 Key Features
- **SHA-256 Integrity Checks:** Automatically generates a unique "fingerprint" for every file uploaded.
- **File Deduplication:** Uses the SHA-256 hash as a unique constraint to prevent redundant storage of identical files.
- **Persistent Metadata:** Stores file names, sizes, upload timestamps, and hashes in a **PostgreSQL** relational database.
- **Automated Documentation:** Built-in interactive API docs via Swagger/OpenAPI.

## 🛠️ Technical Stack
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.13)
- **Database:** [PostgreSQL](https://www.postgresql.org/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Hashing:** Python `hashlib` (SHA-256)
- **Server:** Uvicorn

## 📂 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/shalyariddhi/secure-file-metadata-api.git](https://github.com/shalyariddhi/secure-file-metadata-api.git)
   cd secure-file-metadata-api
