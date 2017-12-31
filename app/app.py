from flask import Flask, render_template
from flask_socketio import SocketIO, emit, disconnect
import os

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    emit('socket_response', {'data': 'Connected'})

@socketio.on('disconnect_request')
def disconnect_request():
    emit('socket_response', {'data': 'Disconnected!'})
    disconnect()

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('my_event')
def test_message(message):
    emit('socket_response', {'data': message["data"]}, broadcast=True, include_self=False)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True if os.getenv("ENV", "prod") == "dev" else "False")
