from pymongo import MongoClient  # type: ignore
from dotenv import load_dotenv  # type: ignore
import os
load_dotenv()
# print(os.getenv('MONGODB_URI'))
client=MongoClient(os.getenv('MONGODB_URI'))
db = client.dbSparta
