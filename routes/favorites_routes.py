from flask import Blueprint
from controllers.favorites_controller import index, new, create, edit, update, delete, like, comment, favorite

favorites_routes = Blueprint('favorites_routes', __name__)

favorites_routes.route('')(index)
favorites_routes.route('/new')(new)
favorites_routes.route('', methods=["POST"])(create)
favorites_routes.route('/<id>/edit')(edit)
favorites_routes.route('/<id>', methods=["POST"])(update)
favorites_routes.route('/<id>/delete', methods=["POST"])(delete)
favorites_routes.route('/<id>/comments', methods=["POST"])(comment)
favorites_routes.route('/<id>/likes', methods=["POST"])(like)
favorites_routes.route('/<id>/favorites', methods=["POST"])(favorite)