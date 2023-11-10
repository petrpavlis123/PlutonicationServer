from flask import Flask
from .events import socketio
from .extensions import cache
from .router import app

def create_app():
    # Config here
    app.config.from_mapping({
        "DEBUG": False, 
        "CACHE_TYPE": "SimpleCache",  # Flask-Caching related config
        "CACHE_DEFAULT_TIMEOUT": 1  # Flask-Caching related config
    })

    socketio.init_app(app, cors_allowed_origins="*")

    cache.init_app(app)

    return app