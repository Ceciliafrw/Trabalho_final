import sqlite3 as lite

####### criando conexao com banco de dados ##########
con = lite.connect('dados.db')

####### Usuario##########
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO usuario\
             (nome, logradouro, num, bairro, cep, cidade, estado, idade, genero, telefone, cpf, email)\
                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query,i) 

def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM usuario"
        cur.execute(query)
        informacao = cur.fetchall()
        for i in informacao:
            lista.append(i)
    return lista

def atualizar_info(i):

    with con:
        cur = con.cursor()
        query = "UPDATE usuario SET nome=?, email=?, telefone=?,cal=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query,i)   

def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM usuario WHERE id=?"
        cur.execute(query,i)   


####### Evento ##########
def inserir_info_evento(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO evento\
             (evento, data, cidade, estado, local, espaco, tipo, valor, descricao)\
                  VALUES (?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query,i) 
  
def mostrar_info_evento():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM evento"
        cur.execute(query)
        informacao = cur.fetchall()
        for i in informacao:
            lista.append(i)
    return lista

def atualizar_info_evento(i):

    with con:
        cur = con.cursor()
        query = "UPDATE evento SET evento=?, data=?, cidade=?, estado=?, local=?, espaco=?, tipo=?, valor=?,\
             descricao WHERE id=?"
        cur.execute(query,i)   

def deletar_info_evento(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM evento WHERE id=?"
        cur.execute(query,i)   



####### Agenda ##########
def inserir_info_agenda(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO agenda\
             (nome_completo, idade, email, usuario_id, evento_id)\
                  VALUES (?,?,?,?,?)"
        cur.execute(query,i) 
  
def mostrar_info_agenda():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM agenda"
        cur.execute(query)
        informacao = cur.fetchall()
        for i in informacao:
            lista.append(i)
    return lista

def atualizar_info_agenda(i):

    with con:
        cur = con.cursor()
        query = "UPDATE agenda SET nome_completo=?, idade=?, email=? usuario_id=?, evento_id=?)\
             descricao WHERE id=?"
        cur.execute(query,i)   

def deletar_info_agenda(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM agenda WHERE id=?"
        cur.execute(query,i)   
