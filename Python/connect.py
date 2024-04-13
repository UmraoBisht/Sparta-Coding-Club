from pymongo import MongoClient


url='mongodb+srv://umraobisht:5PRL0pgA745Z5Bf7@cluster0.xcolmec.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client=MongoClient(url)

db=client.dbSparta

# doc={
#     "name":'umrao',
#     "enroll_number":43
# }
# db.users.insert_one(doc)