from pymongo import MongoClient  # type: ignore
import os
from dotenv import load_dotenv  # type: ignore
load_dotenv()

url = os.getenv("MONGODB_URL")
client = MongoClient(url)
db = client.dbSparta

