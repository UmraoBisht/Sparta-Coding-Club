from connect import db
doc1={
    "name":'Ankit',
    "enroll_number":34
}
doc2={
    "name":'Deepak',
    "enroll_number":42
}
doc3={
    "name":'Vipin',
    "enroll_number":57
}
doc4={
    "name":'Kartik',
    "enroll_number":48
}
doc5={
    "name":'Lakshaya',
    "enroll_number":49
}

# db.users.insert_one(doc1)
# db.users.insert_one(doc2)
# db.users.insert_one(doc3)
# db.users.insert_one(doc4)
# db.users.insert_one(doc5)

docs=[
    {'title':"Harry Potter",
    'author':"J.K Rowling",
    'rating':90
    },
    {'title':"The Fisherman and Fish",
    'author':'Joseph Choi',
    'rating':10
    },
    {'title':"Fire in the Water",
    'author':'Some Dude',
    'rating':57
    }
]


# db.users.update_one({'name':'umrao'},{'$set':{'enroll_number':44}})
# db.users.delete_one({'name':'Lakshaya'})

# for doc in docs:
#     db.books.insert_one(doc)


db.books.update_one({'title':'The Fisherman and Fish'},{'$set':{'author':'Jimmy Kim'}})
db.books.delete_one({'rating':90})

# all_users=list(db.users.find({},{'_id':False}))
# print(all_users)