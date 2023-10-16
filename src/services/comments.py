# import for libraries
from flask import request, Response
from bson import json_util, ObjectId

# import form src
from config.mongodb import mongo

def create_comment_service():
    data = request.get_json()
    author_comment = data.get('author', None)
    comment = data.get('text', None)
    date = data.get('date', None)
    content = data.get('content', None)
    if author_comment:
        response = mongo.db.Comments.insert_one({
            'author' : author_comment,
            'text': comment,
            'date': date,
            'content': content,
            'point': False
        })
        result = {
            'id': str(response.inserted_id),
            'author' : author_comment,
            'text': comment,
            'date': date,
            'content': content,
            'point': False
        }
        return result
    else:
        return 'Invalid payload', 400    
    
def get_comments_service():
    data = mongo.db.Comments.find()
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

def get_comment_service(id):
    data= mongo.db.Comments.find_one({'_id':ObjectId(id)})
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

def update_comment_service(id):
    data = request.get_json()
    if len(data)==0:
        return 'Invalid payload', 400
    
    response = mongo.db.Comments.update_one({'_id':ObjectId(id)}, {'$set':data})
    
    if response.modified_count>=1:
        result = 'comment updated successfully'
        return result, 200
    else:
        return 'comment not found', 404
    
def delete_comment_service(id):
    response = mongo.db.Comments.delete_one({'_id':ObjectId(id)})
    if response.deleted_count >= 1:
        return 'comment deleted successfully'
    else:
        return 'comment not found', 404
    