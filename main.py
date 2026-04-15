import hashlib
from fastapi import FastAPI, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Metadata API")

@app.post("/upload/")
async def upload_file(file: UploadFile, db: Session = Depends(get_db)):
    # 1. Read file content
    content = await file.read()
    
    # 2. Calculate SHA-256 Hash
    sha256_hash = hashlib.sha256(content).hexdigest()
    
    # 3. Check if this exact file was already uploaded
    existing_file = db.query(models.FileMetadata).filter(models.FileMetadata.sha256_hash == sha256_hash).first()
    if existing_file:
        return {"message": "File already exists", "metadata": existing_file}

    # 4. Save metadata to Postgres
    db_file = models.FileMetadata(
        filename=file.filename,
        file_size=len(content),
        sha256_hash=sha256_hash
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    return {"status": "Success", "hash": sha256_hash, "details": db_file}

@app.get("/files/")
def get_all_metadata(db: Session = Depends(get_db)):
    return db.query(models.FileMetadata).all()