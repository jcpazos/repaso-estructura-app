from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import models, topRoutes

from app.routes.login_bp import login_bp
from app.routes.users_bp import users_bp

app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(users_bp, url_prefix="/users")

db.create_all()