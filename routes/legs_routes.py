from flask import Blueprint
from controllers.legs_controller import index, new, create, edit, update, delete, comment, favourite

legs_routes = Blueprint('legs_routes', __name__)

legs_routes.route('')(index)
legs_routes.route('/new')(new)
legs_routes.route('', methods=["POST"])(create)
legs_routes.route('/<id>/edit')(edit)
legs_routes.route('/<id>', methods=["POST"])(update)
legs_routes.route('/<id>/delete', methods=["POST"])(delete)
legs_routes.route('/<id>/comments', methods=["POST"])(comment)
legs_routes.route('/<id>/favourites', methods=["POST"])(favourite)