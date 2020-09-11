import datetime
from app import db, ma


class Users(db.Model):
    """ Definição da classe/tabela dos usuários e seus campos"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name


class UsersSchema(ma.Schema):
    """ Definindo o Schema do Marshmallow para facilitar a utilização de JSON """
    class Meta:
        fields = ('id', 'username', 'name', 'password', 'created_on')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
