from flask import Flask, render_template, request, redirect
from pessoa import Pessoa
from tipo_transporte import Transporte
from destino import Destino
from distancia import Distancia
from valor import Valores
import MySQLdb

####################         ########   PESSOA    ################   ####################



def cadastrar_pessoa_db(cpf, nome):   
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO pessoa (cpf , nome)" + 
    " VALUES ('{}', '{}')".format(cpf, nome))
    conexao.commit()
    pessoa_id = cursor.lastrowid
    conexao.close()
    return pessoa_id

def listar_pessoa_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pessoa")
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
    cursor.execute("DELETE FROM pessoa WHERE id={}".format(id))
    conexao.commit()
    conexao.close()

def alterar_pessoa_db(pessoa:Pessoa):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("UPDATE pessoa SET( cpf='{}', nome='{}') WHERE id={}"
    .format(pessoa.cpf, pessoa.nome, pessoa.id))
    conexao.commit()
    conexao.close()

def buscar_pessoa_por_id(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM pessoa WHERE id ={}'.format(id))
    p = Pessoa()
    for i in cursor.fetchall():
        p.id = i[0]
        p.cpf = i[1]
        p.nome = i[2]
    conexao.close()
    return p

#########  #############     TIPO_TRANSPORTE           ##################   ########



def cadastrar_tipo_transporte_db(pessoaid, tipo):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tipo_transporte (tipo, pessoa_id) VALUES ('{}', '{}')".format(tipo, pessoaid))
    conexao.commit()
    transporte_id = cursor.lastrowid
    conexao.close()
    return transporte_id

def listar_tipo_transporte_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tipo_transporte")
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
    cursor.execute("UPDATE pessoa SET( pessoa_id='{}', TIPO='{}') WHERE id={}"
    .format(tipo_transporte.pessoa_id, tipo_transporte.tipo, tipo_transporte.id))
    conexao.commit()
    conexao.close()


def deletar_tipo_transporte():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tipo_transporte WHERE id={}".format(id))
    conexao.commit()
    conexao.close()



def buscar_tipo_transporte_por_id(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tipo_transporte WHERE id ={}'.format(id))
    t = Transporte()
    for i in cursor.fetchall():
        t.id = i[0]
        t.pessoa_id = i[1]
        t.tipo = i[2]
    conexao.close()
    return t    



#####        ###########    DESTINO    ###########       #######



def cadastrar_destino_trans_db(trans_id, inicial, final):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO destino (destino_trans_id, inicial, final)" + 
    " VALUES ('{}', '{}','{}')".format(trans_id , inicial , final))
    conexao.commit()
    destino_id = cursor.lastrowid
    conexao.close()
    return destino_id

def listar_destino_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("SELECT * destino")
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
    cursor.execute("UPDATE destino SET( destino_trans_id ='{}', inicial='{}', final='{}') WHERE id={}"
    .format(destino.destino_trans_id, destino.inicial,  destino.final, destino.id))
    conexao.commit()
    conexao.close()


def deletar_destino():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM destino WHERE id={}".format(id))
    conexao.commit()
    conexao.close()



def buscar_em_destino(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM destino WHERE id ={}'.format(id))
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

def cadastrar_distancia_trans_db(trans_id, km):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO distancia (distancia_trans_id, km) VALUES ('{}', '{}')".format(trans_id , km))
    conexao.commit()
    conexao.close()


def listar_distancia_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("SELECT * distancia")
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
    cursor.execute("UPDATE distancia SET( distancia_trans_id='{}', km='{}') WHERE id={}"
    .format(distancia.distancia_trans_id, distancia.km,  distancia.id))
    conexao.commit()
    conexao.close()


def deletar_distancia():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM distancia WHERE id={}".format(id))
    conexao.commit()
    conexao.close()



def buscar_em_distancia(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM distancia WHERE id ={}'.format(id))
    dist = Distancia()
    for i in cursor.fetchall():
        dist.id = i[0]
        dist.distancia_trans_id = i[1]
        dist.km = i[2]
    conexao.close()
    return dist



##############################  VALOR ############################### VALOR ######################### VALOR ############################# ##############################
#########################################################################################################################################################################

valores = Valores()

def cadastrar_valores_db(trans_id, valor_recebido):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO valor (valor_trans_id, valor) VALUES ('{}', '{}')".format(trans_id , valor_recebido))
    conexao.commit()
    conexao.close()
    

def listar_valores_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("SELECT * valor")
    listar_valor = []
    for i in cursor.fetchall():
        valores = Valores()
        valores.id = i[0]
        valores.valores_trans_id= i[1]
        valores.valor= i[2]
        listar_valor.append(valores)    
    conexao.close()
    return listar_valor

def editar_valor_db(valores:Valores):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("UPDATE valor SET( valor_trans_id='{}', valor='{}') WHERE id={}"
    .format(valores.valores_trans_id, valores.valor,  valores.id))
    conexao.commit()
    conexao.close()


def deletar_valor():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM valor WHERE id={}".format(id))
    conexao.commit()
    conexao.close()



def buscar_em_valores(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae06", passwd="grupo01", database="zuplae06")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM valor WHERE id ={}'.format(id))
    valor = Valores()
    for i in cursor.fetchall():
        valor.id = i[0]
        valor.valores_trans_id = i[1]
        valor.valor = i[2]
    conexao.close()
    return valor



#####ROTAS###

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/geral/salvar' , methods=['POST'])
def salvar_todos():
    nome = request.form['nome']
    cpf = request.form['cpf']
    tipo_trans = request.form['tipo']   
    destino_inicial = request.form['inicial']
    destino_final = request.form['final']  
    km = request.form['km']  
    valor = request.form['valor']
    pessoa = Pessoa()
    pessoa.nome = nome
    pessoa.cpf = cpf 
    id_pessoa = cadastrar_pessoa_db(pessoa.nome, pessoa.cpf)  
    #ao invés de passar como parâmetro o objeto todo, estou passando cada característica.   
    tipodetransporte = Transporte()
    tipodetransporte.pessoa_id = id_pessoa
    tipodetransporte.tipo = tipo_trans
    tipo_transporte_id =  cadastrar_tipo_transporte_db(tipodetransporte.pessoa_id, tipodetransporte.tipo)    
    #ao invés de passar como parâmetro o objeto todo, estou passando cada característica.
    destino = Destino()
    destino.destino_trans_id = tipo_transporte_id
    destino.inicial = destino_inicial
    destino.final = destino_final
    cadastrar_destino_trans_db(destino.destino_trans_id, destino.inicial, destino.final)
    #ao invés de passar como parâmetro o objeto todo, estou passando cada característica.   
    distancia = Distancia()
    distancia.distancia_trans_id = tipo_transporte_id
    distancia.km = km
    cadastrar_distancia_trans_db(distancia.distancia_trans_id, distancia.km)
    #ao invés de passar como parâmetro o objeto todo, estou passando cada característica.
    valor1 = Valores()
    valor1.valores_trans_id = tipo_transporte_id
    valor1.valores = valor
    cadastrar_valores_db(valor1.valores_trans_id, valor1.valores)
    #ao invés de passar como parâmetro o objeto todo, estou passando cada característica.
    return redirect('/')

    

@app.route('/lista')
def listar():
    return render_template('listar.html')

app.run()