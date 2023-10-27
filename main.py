from plutonication import create_app, socketio

print("Starting Flask")

app = create_app()

if __name__ == "__main__":
    app.debug = True
    socketio.run(app, host="0.0.0.0")
