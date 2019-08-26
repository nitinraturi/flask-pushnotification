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

    token = '{"endpoint":"https://fcm.googleapis.com/fcm/send/cn2zZ1wyZmU:APA91bEBokYMmP36-gLljRWai79Uc6WOxqjum1ztj-Wm6JTkIf6DbtO05R2uXe7O1RfKYZqp0uRZR3K36-7UP-X3FeVR2Wy4NIGYHjiVLSWML8ETGdHA8UNhv5hMJWI7WJcEv1tpce0v","expirationTime":null,"keys":{"p256dh":"BDRC9vUDGoGzt8gefuR5qTPsT3_st_bU8sPj970T5xmY7RjtAVf6Yof1AwS3D6p3U3JmAqpukF7V_VC5uQw5Nec","auth":"MJNVm_d4GJblbEb9PuirJA"}}'
    message = "hello"

    print("token",token)
    print("message",message)
    try:
        send_web_push(json.loads(token), message)
    except Exception as e:
        print("error",e)

    return redirect(url_for('main.index'))
