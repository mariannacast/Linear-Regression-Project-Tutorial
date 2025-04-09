from utils import db_connect
from models.user_model import User
from sqlalchemy.orm import declarative_base

Base = User.__bases__[0]
engine = db_connect()

# ✅ This must be here to create the table
Base.metadata.create_all(engine)

print("✅ Database tables created successfully.")
