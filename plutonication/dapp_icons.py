from flask import send_file
from .extensions import app


@app.route("/dapp/hydradx-icon")
def hydradx_icon():
    return send_file("static/dapp_icons/hydradx-icon.png", mimetype='image/png')

