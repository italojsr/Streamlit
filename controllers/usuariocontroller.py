import services.database as db

def Incluir(usuario):
    count = db.cursor.execute("""
    INSERT INTO Usuario (CPF, Nome, Telefone, Email) 
    VALUES (?,?,?,?)""",
    usuario.cpf,usuario.nome,usuario.telefone,usuario.email).rowcount
    db.cnxn.commit()

