import os
from pywebpush import webpush, WebPushException
from settings import *

VAPID_CLAIMS = {
"sub": "mailto:hralgofins@gmail.com"
}

def send_web_push(subscription_information, message_body):
    return webpush(
        subscription_info=subscription_information,
        data=message_body,
        # vapid_private_key=VAPID_PRIVATE_KEY,
        # vapid_claims=VAPID_CLAIMS
    )
