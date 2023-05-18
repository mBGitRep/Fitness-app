from flask import Blueprint
from controllers.exercises_controller import index, new, create, edit, update, delete, like, comment, favorite

exercises_routes = Blueprint('exercises_routes', __name__)

exercises_routes.route('')(index)
exercises_routes.route('/new')(new)
exercises_routes.route('', methods=["POST"])(create)
exercises_routes.route('/<id>/edit')(edit)
exercises_routes.route('/<id>', methods=["POST"])(update)
exercises_routes.route('/<id>/delete', methods=["POST"])(delete)
exercises_routes.route('/<id>/comments', methods=["POST"])(comment)
exercises_routes.route('/<id>/likes', methods=["POST"])(like)
exercises_routes.route('/<id>/favorites', methods=["POST"])(favorite)