from flask import Blueprint
from controllers.shoulders_controller import index, new, create, edit, update, delete, comment, favourite

shoulders_routes = Blueprint('shoulders_routes', __name__)

shoulders_routes.route('')(index)
shoulders_routes.route('/new')(new)
shoulders_routes.route('', methods=["POST"])(create)
shoulders_routes.route('/<id>/edit')(edit)
shoulders_routes.route('/<id>', methods=["POST"])(update)
shoulders_routes.route('/<id>/delete', methods=["POST"])(delete)
shoulders_routes.route('/<id>/comments', methods=["POST"])(comment)
shoulders_routes.route('/<id>/favourites', methods=["POST"])(favourite)