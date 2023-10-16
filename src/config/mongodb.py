from flask_pymongo import PyMongo
# import pymongo

mongo = PyMongo()

# # from pymongo import MongoClient

# # Establish a connection to the MongoDB server
# client = MongoClient()

# # Access the desired database
# db = client.spacio

# # Access the collection within the database
# collection = db.comments

# # Insert a document into the collection
# document = {"name": "John", "age": 30}
# collection.insert_one(document)
# print("Document inserted successfully.")

# # Retrieve documents from the collection
# documents = collection.find()
# print("Documents in the collection:")
# for doc in documents:
#    print(doc)

# # Update a document in the collection
# collection.update_one({"name": "John"}, {"$set": {"age": 35}})
# print("Document updated successfully.")

# # Retrieve the updated document
# updated_doc = collection.find_one({"name": "John"})
# print("Updated Document:")
# print(updated_doc)

# # Delete a document from the collection
# collection.delete_one({"name": "John"})
# print("Document deleted successfully.")

# # Verify the deletion by retrieving the document again
# deleted_doc = collection.find_one({"name": "John"})
# print("Deleted Document:")
# print(deleted_doc)

# # Close the MongoDB connection
# client.close()