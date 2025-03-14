from flask import Flask, render_template, redirect, url_for, request
import socket_server

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_conexion', methods=['POST'])
def crear_conexion():
    socket_server.start_socket_server()
    return redirect(url_for('conection'))

@app.route('/conection')
def conection():
    return render_template('conection.html', ip=socket_server.IP, port=socket_server.PORT)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', msg='')

@app.route('/go_dashboard')
def go_dashboard():
    return redirect(url_for('dashboard'))
    
@app.route('/close_conection')
def close_conection():
    socket_server.stop_socket_server()
    return redirect(url_for('index'))

@app.route('/send_message', methods=['POST'])
def send_message():
    message = message = request.form.get('message', '')
    if message:
        socket_server.send_message(message)
    return render_template('dashboard.html', msg=message)


# Apagar socket cuando se detenga Flask
import atexit
atexit.register(socket_server.stop_socket_server)

if __name__ == '__main__':
    app.run(debug=True)
