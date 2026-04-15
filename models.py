from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class FileMetadata(Base):
    __tablename__ = "file_metadata"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    file_size = Column(Integer)  # in bytes
    sha256_hash = Column(String, unique=True) # The digital fingerprint
    upload_time = Column(DateTime, default=datetime.datetime.utcnow)