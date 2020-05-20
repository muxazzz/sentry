import os
import random
import json
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

from bottle import route, run

@route("/success")
def index():
  return "hello"

@route("/fail")
def index():
    raise RuntimeError("There is an error")  
    return 

sentry_sdk.init(
    dsn="https://9cb3f344e7344d06a1b0885e97910939@o395254.ingest.sentry.io/5248120",
    integrations=[BottleIntegration()]
)

if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
