import psycopg2
from flask import jsonify

con = psycopg2.connect(database='bd_varejao', user='postgres',
                       password='p0rt31r0')

with con:

    cur = con.cursor()


def insere_dados_postgres(sql, val):
    try:
        cur.executemany(sql, val)
        con.commit()
    except:
        return jsonify({'message': 'Erro no banco de dados Postgres'}), 500
    fecha_sessao()


def fecha_sessao():
    if(con):
        cur.close()
        con.close()
        print("PostgreSQL connection is closed")