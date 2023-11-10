from flask import render_template
from .extensions import app

@app.route("/")
def main_page():
    return render_template("main_page.html")

@app.route("/docs")
def docs_page():
    return render_template("docs_page.html")
