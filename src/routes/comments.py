from flask import Blueprint

from services.comments import delete_comment_service, update_comment_service, create_comment_service, get_comments_service, get_comment_service


comments = Blueprint('Comments', __name__)

@comments.route('/', methods=['GET'])
def get_comments():
    return get_comments_service()

@comments.route('/<id>', methods=['GET'])
def get_comment_by_id(id):
    return get_comment_service(id)


@comments.route('/', methods=['POST'])
def create_comment():
    return create_comment_service()

@comments.route('/<id>', methods=['PUT'])
def update_comment(id):
    return update_comment_service(id)

@comments.route('/<id>', methods=['DELETE'])
def delete_comment(id):
    return delete_comment_service(id)