import sqlite3

from app import Tempo


class SqliteTempo(Tempo):


    URL_DB = 'db/historico.db'

    @staticmethod
    def criar_conexao():

        conexao = None

        try:
            conexao = sqlite3.connect(SqliteTempo.URL_DB)
        except sqlite3.Error as err:
            raise Exception(err)
        return conexao

    def adicionar(self,tempo):
        conexao = SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()

        query = 'INSERT INTO Cotacao VALUES (NULL, ?, ?, ?)'
        #registro = (tempo.informar_data_hora,tempo.informar_temp_atual,tempo.informar_umidade,,tempo.informar_desc_temp,,tempo.informar_velocid_vento)

        try:
            cursor.execute(query,registro)
            conexao.commit()
        except sqlite3.Error as err:
            raise Exception(f'ERRO: {err}')
        finally:
            if conexao:
                conexao.close()
