from flask import Flask, render_template, request, redirect
from pessoa import Pessoa
from tipo_transporte import Transporte
from destino import Destino
from distancia import Distancia
from valor import Valor
import MySQLdb

####################         ########   PESSOA    ################   ####################

pessoa = Pessoa()

def cadastrar_pessoa_db(pessoa):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO PESSOA ('CPF' , 'NOME') VALUES ('{}', '{}')".format(pessoa.cpf, pessoa.nome))
    conexao.commit()
    conexao.close()

def listar_pessoa_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM PESSOA")
    listar_pessoa = []
    for i in cursor.fetchall():
        pessoa = Pessoa()
        pessoa.id = i[0]
        pessoa.cpf = i[1]
        pessoa.nome= i[2]
        listar_pessoa.append(pessoa)
    
    conexao.close()
    return listar_pessoa


def deletar_pessoa(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM PESSOA WHERE id={}".format(id))
    conexao.commit()
    conexao.close()

def alterar_pessoa_db(pessoa:Pessoa):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("UPDATE PESSOA SET( CPF='{}', NOME='{}') WHERE ID={}"
    .format(pessoa.cpf, pessoa.nome, pessoa.id))
    conexao.commit()
    conexao.close()

def buscar_pessoa_por_id(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM PESSOA WHERE ID ={}'.format(id))
    p = Pessoa()
    for i in cursor.fetchall():
        p.id = i[0]
        p.cpf = i[1]
        p.nome = i[2]
    conexao.close()
    return p

#########  #############     TIPO_TRANSPORTE           ##################   ########

tipo_transporte = Transporte()

def cadastrar_tipo_transporte_db(Transporte):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO TIPO_TRANSPORTE ('PESSOA_ID' ,'TIPO') VALUES ('{}', '{}')".format(tipo_transporte.pessoa_id , tipo_transporte.tipo))
    conexao.commit()
    conexao.close()

def listar_tipo_transporte_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM TIPO_TRANSPORTE")
    listar_tipo_transporte = []
    for i in cursor.fetchall():
        tipo_transporte = Transporte()
        tipo_transporte.id = i[0]
        tipo_transporte.pessoa_id = i[1]
        tipo_transporte.tipo = i[2]
        listar_tipo_transporte.append(tipo_transporte)    
    conexao.close()
    return listar_tipo_transporte

def editar_tipo_transporte_por_id_db(tipo_transporte:Transporte):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("UPDATE PESSOA SET( PESSOA_ID='{}', TIPO='{}') WHERE ID={}"
    .format(tipo_transporte.pessoa_id, tipo_transporte.tipo, tipo_transporte.id))
    conexao.commit()
    conexao.close()


def deletar_tipo_transporte():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM TIPO_TRANSPORTE WHERE ID={}".format(id))
    conexao.commit()
    conexao.close()



def buscar_tipo_transporte_por_id(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM TIPO_TRANSPORTE WHERE ID ={}'.format(id))
    t = Transporte()
    for i in cursor.fetchall():
        t.id = i[0]
        t.pessoa_id = i[1]
        t.tipo = i[2]
    conexao.close()
    return t    



#####        ###########    DESTINO    ###########       #######

destino = Destino()

def cadastrar_destino_trans_db(Transporte):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO DESTINO ('DESTINO_TRANS_ID' ,'INICIAL','FINAL') VALUES ('{}', '{}','{}')".format(destino.destino_trans_id , destino.inicial , destino.final))
    conexao.commit()
    conexao.close()

def listar_destino_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("SELECT * DESTINO")
    listar_destino = []
    for i in cursor.fetchall():
        destino = Destino()
        destino.id = i[0]
        destino.inicial = i[1]
        destino.final = i[2]
        listar_destino.append(destino)    
    conexao.close()
    return listar_destino

def editar_destino_db(destino:Destino):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("UPDATE DESTINO SET( DESTINO_TRANS_ID='{}', INICIAL='{}', FINAL='{}') WHERE ID={}"
    .format(destino.destino_trans_id, destino.inicial,  destino.final, destino.id))
    conexao.commit()
    conexao.close()


def deletar_destino():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM DESTINO WHERE ID={}".format(id))
    conexao.commit()
    conexao.close()



def buscar_em_destino(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM DESTINO WHERE ID ={}'.format(id))
    d = Destino()
    for i in cursor.fetchall():
        d.id = i[0]
        d.destino_trans_id = i[1]
        d.inicial = i[2]
        d.final = i[3]
    conexao.close()
    return d


################ DISTANCIA ######################### DISTANCIA ########################### DISTANCIA ############################

distancia = Distancia()

def cadastrar_distancia_trans_db(Transporte):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO DISTANCIA ('DISTANCIA_TRANS_ID' ,'KM') VALUES ('{}', '{}')".format(distancia.distancia_trans_id , distancia.km))
    conexao.commit()
    conexao.close()

def listar_distancia_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("SELECT * DISTANCIA")
    listar_distancia = []
    for i in cursor.fetchall():
        distancia = Distancia()
        distancia.id =i[0]
        distancia.distancia_trans_id = i[1]
        distancia.km = i[2]
        listar_distancia.append(distancia)    
    conexao.close()
    return listar_distancia

def editar_distancia_db(distancia:Distancia):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("UPDATE DISTANCIA SET( DISTANCIA_TRANS_ID='{}', KM='{}') WHERE ID={}"
    .format(distancia.distancia_trans_id, distancia.km,  distancia.id))
    conexao.commit()
    conexao.close()


def deletar_distancia():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM DISTANCIA WHERE ID={}".format(id))
    conexao.commit()
    conexao.close()



def buscar_em_distancia(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM DISTANCIA WHERE ID ={}'.format(id))
    dist = Distancia()
    for i in cursor.fetchall():
        dist.id = i[0]
        dist.distancia_trans_id = i[1]
        dist.km = i[2]
    conexao.close()
    return dist



##############################  VALOR ############################### VALOR ######################### VALOR ############################# ##############################


valores = Valores()

def cadastrar_valores_db(Transporte):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO VALORES ('VALOR_TRANS_ID' ,'VALOR') VALUES ('{}', '{}')".format(distancia.distancia_trans_id , distancia.km))
    conexao.commit()
    conexao.close()

def listar_distancia_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("SELECT * DISTANCIA")
    listar_distancia = []
    for i in cursor.fetchall():
        distancia = Distancia()
        distancia.id[0]
        distancia.distancia_trans_id[1]
        distancia.km[2]
        listar_distancia.append(distancia)    
    conexao.close()
    return listar_distancia

def editar_distancia_db(distancia:Distancia):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("UPDATE DISTANCIA SET( DISTANCIA_TRANS_ID='{}', KM='{}') WHERE ID={}"
    .format(distancia.distancia_trans_id, distancia.km,  distancia.id))
    conexao.commit()
    conexao.close()


def deletar_distancia():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM DISTANCIA WHERE ID={}".format(id))
    conexao.commit()
    conexao.close()



def buscar_em_distancia(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM DISTANCIA WHERE ID ={}'.format(id))
    dist = Distancia()
    for i in cursor.fetchall():
        dist.id = i[0]
        dist.distancia_trans_id = i[1]
        dist.km = i[2]
    conexao.close()
    return dist



#####ROTAS###

