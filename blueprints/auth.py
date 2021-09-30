from flask import Blueprint, request
from flask.json import jsonify
from models import *


bp = Blueprint('auth', __name__,)

@bp.route('/login', methods=['POST'])
def Login():
    if not  request.is_json:
        return jsonify(msg="Missing JSON in headers")

    _username = request.json.get('username', -1)
    _password = request.json.get('password', -1)

    if _username == -1 or _password == -1:
        return jsonify({"msg" : "Missing Something"}), 400

    try:
       user = User.get(User.username == _username)
    except:
        return jsonify({"msg" : "USER NOT FOUND"}), 404

    if user.password != _password:
        return jsonify({"msg" : "PASSWORD WRONG"}), 404
    
    return jsonify(msg="Logged in")

@bp.route('/register', methods=['POST'])
def Register():
    if not  request.is_json:
        return jsonify(msg="Missing JSON in headers")

    _username = request.json.get('username')
    _password = request.json.get('password')

    if _username == -1 or _password == -1:
        return jsonify({"msg" : "Missing Something"}), 400

    user = User(username = _username, password = _password)
    user.save()
    return jsonify('User Created')

if __name__ == '__main__':
    bp.run()