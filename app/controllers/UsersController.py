from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import User
import json
import datetime

def getUsers():
    users = User.query.all()

    allUsers = []

    for user in users:
        allUsers.append({"username": user.username, "email": user.email})

    return json.dumps(allUsers)