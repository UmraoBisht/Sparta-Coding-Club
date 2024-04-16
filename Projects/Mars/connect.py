from pymongo import MongoClient # type: ignore
from dotenv import load_dotenv # type: ignore
import os
load_dotenv()
client=MongoClient(os.getenv('MONGODB_URI'))
# print(client)
db=client.dbSparta