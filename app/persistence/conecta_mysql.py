import mysql.connector
from flask import jsonify

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="p0rt31r0",
    database="bd_macapa"
)

mycursor = mydb.cursor()


def insere_dados_mysql(sql, val):
    try:
        mycursor.executemany(sql, val)
        mydb.commit()
        return jsonify({'message': 'data successfully inserted'}), 201
    except:
        return jsonify({'message': 'unable to insert data'}), 500


print(mycursor.rowcount, "records inserted.")
