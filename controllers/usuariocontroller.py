import services.database as db
import models.Usuario as usuario

def Incluir(usuario):
    count = db.cursor.execute("""
    INSERT INTO usuario (cpf, nome,email,telefone) 
    VALUES (?,?,?,?)""",
    usuario.cpf,usuario.nome,usuario.email,usuario.telefone).rowcount
    db.cnxn.commit()

def SelecionarByCpf(cpf):
    db.cursor.execute("SELECT *FROM usuario WHERE CPF = ?",cpf)
    costumerList = []

    for row in db.cursor.fetchall(): #Fetchall passa as linhas da tabela 
        costumerList.append(usuario.Usuario(row[0],row[1],row[2],row[3]))
    
    return costumerList[0]


def Alterar(usuario):
    count = db.cursor.execute("""
    UPDATE usuario
    SET cpf = ?,nome = ?,email = ?,telefone = ?
    WHERE cpf = ?
    """,usuario.cpf,usuario.nome,usuario.email,usuario.telefone,usuario.cpf).rowcount
    db.cnxn.commit()


def Deletar(cpf):
    count = db.cursor.execute("""
    DELETE FROM USUARIO WHERE cpf = ?""",
    cpf).rowcount
    db.cnxn.commit()

def Incluir(usuario):
    count = db.cursor.execute("""
    INSERT INTO usuario (cpf, nome,email,telefone) 
    VALUES (?,?,?,?)""",
    usuario.cpf,usuario.nome,usuario.email,usuario.telefone).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT *FROM usuario")
    costumerList = []

    for row in db.cursor.fetchall(): #Fetchall passa as linhas da tabela 
        costumerList.append(usuario.Usuario(row[0],row[1],row[2],row[3]))
    
    return costumerList


