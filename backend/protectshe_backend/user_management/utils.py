from protectshe_backend import settings

# Access the MongoDB database
db = settings.mongo_db

def test_mongo_connection():
    # Insert a test document
    db.test_collection.insert_one({"message": "MongoDB connection successful!"})
    # Retrieve the document
    return db.test_collection.find_one({"message": "MongoDB connection successful!"})
