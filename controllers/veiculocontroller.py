import services.database_veiculo as db
import models.Veiculo as veiculo

def Incluir(veiculo):
    count = db.cursor.execute("""
    INSERT INTO veiculo (tipo, modelo, marca,ano,quilometragem,preco) 
    VALUES (?,?,?,?,?,?)""",
    veiculo.tipo,veiculo.modelo,veiculo.marca,veiculo.ano,veiculo.quilometragem, veiculo.preco).rowcount
    db.cnxn.commit()
    


def SelecionarById(id):
    db.cursor.execute("SELECT *FROM veiculo WHERE id_anuncio = ?",id)
    costumerList = []

    for row in db.cursor.fetchall(): #Fetchall passa as linhas da tabela 
        costumerList.append(veiculo.Veiculo(row[0],row[1],row[2],row[3], row[4], row[5],row[6]))
    
    return costumerList[0]


def Alterar(veiculo):
    count = db.cursor.execute("""
    UPDATE veiculo
    SET tipo = ?,modelo = ?,marca = ?,ano = ?,quilometragem = ?,preco = ?
    WHERE id_anuncio = ?
    """,veiculo.tipo,veiculo.modelo,veiculo.marca,veiculo.ano,veiculo.quilometragem,veiculo.preco,veiculo.id).rowcount
    db.cnxn.commit()


def Deletar(id):
    count = db.cursor.execute("""
    DELETE FROM veiculo WHERE id_anuncio = ?""",
    id).rowcount
    db.cnxn.commit()


def SelecionarTodos():
    db.cursor.execute("SELECT *FROM veiculo")
    costumerList = []

    for row in db.cursor.fetchall(): #Fetchall passa as linhas da tabela 
        costumerList.append(veiculo.Veiculo(row[0],row[1],row[2],row[3], row[4], row[5],row[6]))
    
    return costumerList
