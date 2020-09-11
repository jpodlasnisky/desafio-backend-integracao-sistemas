import datetime

import jwt
from werkzeug.security import check_password_hash
from flask import request, jsonify
from functools import wraps

from app import app
from app.views.users import user_by_username


""" Decorator para checar se foi passado um token para um endpoint. Receberá uma função e
para transformar a função em decorator, é necessário o udo de wraps. O wraps será usado como decorator 
de uma segunda função que irá receber todo e qualquer argumento"""
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # recebe token do cabeçalho ou da url
        #token = request.args.get('token')
        token = request.headers['token']
        if not token:
            return jsonify({'message': 'token is missing', 'data': {}}), 401
        # usa o decode para pegar as informações desse token caso ele seja válido
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = user_by_username(username=data['username'])
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': {}}), 401
        return f(current_user, *args, **kwargs)
    return decorated


def auth():
    # valida cabeçalho de autorização
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'could not verify','WWW-Authenticate':'Basic auth="Login required"'}), 401

    # valida se usuário existe no banco
    user = user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'user not found', 'data': {}}), 401

    # valida senha e cria jwt
    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode({'username': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)},
                           app.config['SECRET_KEY'])
        return jsonify({'message': 'Validated successfully', 'token': token.decode('UTF-8'),
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'could not verify', 'WWW-Authenticate':'Basic auth="Login required"'}), 401
