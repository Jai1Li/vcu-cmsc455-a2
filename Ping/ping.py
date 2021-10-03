import time
import requests
from requests.auth import HTTPDigestAuth
from flask import Flask, jsonify, g
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
auth = HTTPDigestAuth()

global start
start = 0
users = {
    'vcu': 'rams'
}


@auth.get_password
def get_pass(username):
    if username in users:
        return users.get(username)
    return None


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message': 'Page Not Here'}), 404


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message': 'Something is Broke'}), 500


@app.route('/ping', methods=['GET'])
@auth.login_required
def ping_service():
    url = ' https://vcu-cmsc455-a2.herokuapp.com/'
    start_time()
    requests.get(url, auth=requests.auth.HTTPDigestAuth('vcu', 'rams'))
    time_elps = jsonify(pingpong_t=(end_time()*1000))
    return time_elps.json, 201

def start_time():
    g.start = time.time()
    return g.start


def end_time():
    return time.time() - g.start
