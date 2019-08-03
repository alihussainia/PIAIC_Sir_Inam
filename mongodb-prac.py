from pymongo import MongoClient
#mongodb://uid:pass@localhost:27017/test-db
client = MongoClient('mongodb+srv://inampaki:Pakistan@cluster0-nlrwe.mongodb.net/test?retryWrites=true&w=majority')
db = client['test-db']

posts = db.posts
# post = {'Name': 'Aqsa', 'Class': 'CNCF'}
# posts.insert_one(post)
# post = {'Name': 'aqsa', 'Class': 'AI'}
# print(posts.insert_one(post).inserted_id)
# print(db.list_collection_names())
cursor_posts = db.posts.find({'Name': 'Inam-ul-Haq'})
for post in cursor_posts:
    print(post)

#db.posts.update({'Name': 'Inam'}, {'Name': 'Inam-ul-Haq'}, multi=True)
#db.posts.remove({'Name': 'aqsa'})

