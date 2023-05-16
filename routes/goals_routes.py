from flask import Blueprint
from controllers.goals_controller import index, new, create, edit, update, delete

goals_routes = Blueprint('goals_routes', __name__)

goals_routes.route('')(index)
goals_routes.route('/new')(new)
goals_routes.route('', methods=["POST"])(create)
goals_routes.route('/<id>/edit')(edit)
goals_routes.route('/<id>', methods=["POST"])(update)
goals_routes.route('/<id>/delete', methods=["POST"])(delete)