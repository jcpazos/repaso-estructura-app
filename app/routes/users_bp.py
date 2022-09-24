from flask import Blueprint
from app.controllers.UsersController import getUsers

users_bp = Blueprint('users_bp', __name__)

users_bp.route("/", methods=["GET"]) (getUsers)
#login_bp.route("/update") (update)