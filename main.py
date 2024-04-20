from plutonication import create_app, socketio
from flask_cors import CORS

app = create_app()
CORS(app)

# main method
if __name__ == "__main__":
    socketio.run(host="0.0.0.0", port="8090")
