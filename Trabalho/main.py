from flask import Flask, render_template, request, redirect
from pessoa import Pessoa
import MySQLdb

####   PESSOA

pessoa = Pessoa()

def cadastrar_pessoa_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO PESSOA ('CPF' , 'NOME') VALUES ('{}', '{}')".format(pessoa.cpf, pessoa.nome))
    conexao.commit()
    conexao.close()

def listar_pessoa_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("select * from PESSOA")
    listar_pessoa = []
    for i in cursor.fetchall():
        pessoa = Pessoa()
        pessoa.cpf[0]
        pessoa.nome[1]
        listar_pessoa.append(pessoa)
    
    conexao.close()
    return listar_pessoa



#####ROTAS###

