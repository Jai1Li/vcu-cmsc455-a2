import random
from flask import Flask, jsonify
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
auth = HTTPDigestAuth()


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


@app.route('/pong', methods=['GET'])
@auth.login_required
def pong_service():
    return random(), 201


