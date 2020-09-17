from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__, template_folder='./templates', static_url_path='/static')
app.config['SECRET_KEY'] = 'secret!'
app.config['MESSAGE_LOG'] = False # Turn on to print message logs to the console
socketio = SocketIO(app)

@app.route('/')
def chat_room():
    return render_template('index.html')



@socketio.on('message')
def handle_message(message):
    if app.config['MESSAGE_LOG']:
        print('received message: ' + message)
    send(message, broadcast=True)




if __name__ == '__main__':
    socketio.run(app)
