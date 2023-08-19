from flask import Flask,render_template 
from flask_socketio import SocketIO, emit
import base64
import numpy as np
from camera.utils import get_decoded_image, get_encoded_image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("index.html")

@socketio.on('image')
def handle_message(data):
    img = get_decoded_image(data["data"])
    x = get_encoded_image(img)
    emit("receiver",{"data":x},broadcast=True)


if __name__ == "__main__":
    socketio.run(app,port=5000)