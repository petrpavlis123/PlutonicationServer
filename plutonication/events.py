from .extensions import socketio
from flask_socketio import join_room, emit
from flask import request


@socketio.on("connect")
def connect():
    """
    Event handler that is fired whenever someone connects.

    Useful for debugging.
    """
    print(request.remote_addr)
    emit("message", "Someone connected <3", broadcast=True)

@socketio.on("disconnect")
def disconnect():
    """
    Event handler that is fired whenever someone disconnects.
    """
    print("Disconnected")
    emit("disconnect", "Someone disconnected :(", broadcast=True)

@socketio.on("create_room")
def create_room(data):
    """
    Creates a new websocket room.

    Docs: https://socket.io/docs/v3/rooms/
    """
    room = data["Room"]
    join_room(room)

@socketio.on("sign_payload")
def sign_payload(data):
    """
    Event handler used by dApps. Used when requesting signature from wallet.

    You can expect that the wallet will emit either "payload_signature" event or "payload_signature_rejected" event
    """
    room = data["Room"]
    emit("sign_payload", data["Data"], room=room)

@socketio.on("sign_raw")
def sign_raw(data):
    """
    Event handler used by dApps. Used when requesting signature from wallet.

    You can expect that the wallet will emit either "raw_signature" event or "raw_signature_rejected" event
    """
    room = data["Room"]
    emit("sign_raw", data["Data"], room=room)

@socketio.on("payload_signature")
def payload_signature(data):
    """
    Event handler used by wallet, when wallet decides to sign given payload.
    """
    room = data["Room"]
    emit("payload_signature", data["Data"], room=room)

@socketio.on("payload_signature_rejected")
def payload_signature_rejected(data):
    """
    Event handler used by wallet, when wallet decides to reject the signing of given payload.
    """
    room = data["Room"]
    emit("payload_signature_rejected", data["Data"], room=room)


@socketio.on("raw_signature")
def raw_signature(data):
    """
    Event handler used by wallet, when wallet decides to sign given raw message.
    """
    room = data["Room"]
    emit("raw_signature", data["Data"], room=room)

@socketio.on("raw_signature_rejected")
def raw_signature_rejected(data):
    """
    Event handler used by wallet, when wallet decides to reject the signing of given raw message.
    """
    room = data["Room"]
    emit("raw_signature_rejected", data["Data"], room=room)

@socketio.on("pubkey")
def pubkey(data):
    """
    The first event emitted by wallet.

    One of the side-effects is joining a given room.
    """
    room = data["Room"]
    join_room(room)
    emit("pubkey", str(data["Data"]), room=room)
