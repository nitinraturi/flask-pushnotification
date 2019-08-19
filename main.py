import logging
import json, os

from flask import request, Response, render_template, Blueprint
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
    message = request.get_json("message") if request.data else "Updates available"
    tt = [
        # '{"endpoint":"https://fcm.googleapis.com/fcm/send/fVvCcm9s4ig:APA91bFBX-6giILFQ2ynGLT8nQXkDQUHphG95XUnc5Cjf5eEYne4iQTHXYhSy_FnJbJ-kNzlh8QukI2ooCpZ_OnUvH_QPLBtL4o3l66tnESJvDnWvye-qW7MPGbXyki161BPznfGAhXC","expirationTime":null,"keys":{"p256dh":"BI1duDSkhkZEedzd5L5pO12FhYlNyyMz_x9dHCB6uZsBweWlaWGBbjH_7CH6J_5pqg1RlHecfZtQQk5S6mpbx3o","auth":"Pkhy3ueraoyaUe-3dkeMSg"}}',
        '{"endpoint":"https://updates.push.services.mozilla.com/wpush/v2/gAAAAABdWnnwfBxveTgw2rHI1R0B-t4SAQOoxSISTiyu2OiI1N55xioNdYUEt2J015bDogI41QZlSZ_7lxm84ggmciv2gkVs0UD3_zwtUk0UnN1w6tdBG9TeuXAJHbDSNTnfmTaVuO-WtWdTKaK2ITDnLCSGVvRfgVuc1i5uXzCoQbGHo0-P3iA","keys":{"auth":"HXq7eB14BGNYF_t3jd8lDQ","p256dh":"BDV3zULf_K2reoELiy5smIcjYylxybl8C0Au33aucoSMcpZi0tW5KrycxT3A0hOwySPVbUJMuPTUgMmI1uEMSWA"}}'
    ]

    for t in tt:
        send_web_push(json.loads(t), message)
    # for user in User.query.all():
    #     print("token",user.subscription_token)
    #     try:
    #         send_web_push(json.loads(user.subscription_token), message)
    #     except Exception as e:
    #         logger.error(e)

    return Response(status=200, mimetype="application/json")
