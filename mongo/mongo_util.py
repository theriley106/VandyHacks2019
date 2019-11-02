# import datetime module
import datetime
# import pymongo module
import pymongo
# connection string
client = pymongo.MongoClient("mongodb+srv://MongoDBUser:vandyHacks123!@queuedup-8aqrb.gcp.mongodb.net/test?retryWrites=true&w=majority")

# test
db = client['SampleDatabase']
# define collection
collection = db['SampleCollection']
# sample data
document = {"company":"Capital One",
"city":"McLean",
"state":"VA",
"country":"US"}
# insert document into collection
id = collection.insert_one(document).inserted_id
print("id")
print(id)
