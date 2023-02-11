from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ********************************************************************
# NOTES
# ********************************************************************
# The following is standard boilerplate code

# Local database
SQLALCHEMY_DATABASE_URL = "sqlite:///./saves.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # Required for SQLite due to multithreading limitations
    # This is interesting because SQLite3, by default,
    # is threadsafe, especially so because of WAL.
    connect_args={"check_same_thread": False}
)

# Declare local session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# For db models and classes
Base = declarative_base()
