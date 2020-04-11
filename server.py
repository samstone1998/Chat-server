from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__, template_folder='./templates', static_url_path='/static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send(message, broadcast=True)




if __name__ == '__main__':
    socketio.run(app, debug=True)
