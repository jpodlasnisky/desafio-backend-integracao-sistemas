import datetime
from app import db, ma


class DadosSchema(ma.Schema):
    class Meta:
        fields = ('name', 'cellphone')


dados_schema = DadosSchema(many=True)
