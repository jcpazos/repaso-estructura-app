from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Login
import datetime

def login():
    body = request.get_json()
    timestamp = datetime.datetime.now()
    print(timestamp)
    login = Login(username=body["username"], timestamp=timestamp)

    try:
        db.session.add(login)
        db.session.commit()
    except Exception as err:
        print(err)
        return {"success":False}

    return {"success":True, "username":login.username, "timestamp": login.timestamp}