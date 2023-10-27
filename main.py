from plutonication import create_app, socketio

print("Starting Flask")

app = create_app()

socketio.run(app, host="0.0.0.0")
