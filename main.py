import logging
import json, os

from flask import request, Response, render_template, Blueprint, redirect, url_for
from flask import jsonify

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from settings import *

from push import send_web_push
from db import *

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route("/subscription/", methods=["GET", "POST"])
def subscription():
    """
        POST creates a subscription
        GET returns vapid public key which clients uses to send around push notification
    """

    if request.method == "GET":
        return Response(response=json.dumps({"public_key": VAPID_PUBLIC_KEY}),
            headers={"Access-Control-Allow-Origin": "*"}, content_type="application/json")

    subscription_token = request.get_json("subscription_token")
    return Response(status=201, mimetype="application/json")

@main.route("/push/", methods=["POST"])
def push_to_all_users():
    token = request.form.get('sub_token')
    message = request.form.get('message')
    print("token",token)
    print("message",message)
    try:
        send_web_push(json.loads(token), message)
    except Exception as e:
        print("error",e)

    return redirect(url_for('main.index'))


@main.route("/push_v1/",methods=['POST'])
def push_v1():
    message = "Push Test v1"
    print("is_json",request.is_json)
    
    if not request.json or not request.json.get('sub_token'):
        return jsonify({'failed':1})

    print("request.json",request.json)

    token = request.json.get('sub_token')
    try:
        send_web_push(json.loads(token), message)
        return jsonify({'success':1})
    except Exception as e:
        print("error",e)

    return jsonify({'failed':str(e)})
