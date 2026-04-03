# backend/models.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import LONGBLOB
import urllib.parse

# ---------------------------------------------------------
#   DATABASE CONFIG
# ---------------------------------------------------------
MYSQL_USER = ""
MYSQL_PASSWORD = ""
MYSQL_HOST = ""
MYSQL_PORT = ""
MYSQL_DB = ""

encoded_pass = urllib.parse.quote_plus(MYSQL_PASSWORD)

DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{encoded_pass}@"
    f"{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

# ---------------------------------------------------------
#   ENGINE + BASE
# ---------------------------------------------------------
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()