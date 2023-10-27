from .extensions import socketio

@socketio.on("connect")
def on_connected(request):
    print("Someone connected")