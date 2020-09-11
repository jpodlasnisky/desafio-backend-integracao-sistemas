from flask import request
from ..persistence.conecta_mysql import insere_dados_mysql
from ..persistence.conecta_postgres import insere_dados_postgres
import re


def format_name_to_upper(string):
    return string.upper()


def format_cellphone(string):
    formatado = re.sub(r'(\d{2})(\d{2})(\d{5})(\d{4})', r'+\1 (\2) \3-\4', string)
    return formatado


def post_json_handler(current_user):
    if request.is_json:
        json_data = request.get_json()
        cliente = current_user
        manipula_dados(cliente, json_data)

    return 'JSON posted'


def manipula_dados(cliente, dados):
    valores = []
    lista = []

    if cliente and dados:
        if cliente == 'Varejão':
            sql = "INSERT INTO contacts (nome, celular) VALUES (%s, %s)"
            for key, values in dados.items():
                for i in range(len(values)):
                    lista.clear()
                    lista.append(values[i]['name'])
                    lista.append(values[i]['cellphone'])
                    tupla = tuple(lista)
                    valores.insert(i, tupla)
            insere_dados_postgres(sql, valores)
        if cliente == 'Macapá':
            sql = "INSERT INTO contacts (nome, celular) VALUES (%s, %s)"
            for key, values in dados.items():
                for i in range(len(values)):
                    lista.clear()
                    lista.append(format_name_to_upper(values[i]['name']))
                    lista.append(format_cellphone(values[i]['cellphone']))
                    tupla = tuple(lista)
                    valores.insert(i, tupla)
            insere_dados_mysql(sql, valores)

    return 'tratou dados'
