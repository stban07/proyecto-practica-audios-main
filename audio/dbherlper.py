import MySQLdb  # pip install mysqlclient
from decouple import config

# Conexion a base de datos mysql
class DBHelper:
    def __init__(self):

        self.mydb = MySQLdb.connect(

            host= config("HOST"),
            user= config("USER"),
            password= config("PASSWORD"),
            database= config("NAME"),
            port=3306
        )

    bdName = 'jostin_bd'


# se insertan los datos a la tabla Estado_animo

    def insert_metronomo(self, usuario_id, audio):
        cursor = self.mydb.cursor()
        query = "INSERT INTO app_vocalizacion(usuario_id, audio) VALUES (%s, %s)"
        valores = (str(usuario_id), audio)
        cursor.execute(query, valores)
        self.mydb.commit()

    def update_audio(self, url_audio):
        cursor = self.mydb.cursor()
        query = "UPDATE app_vocalizacion SET audio = SUBSTRING(%s, 16) WHERE audio = %s"
        valores = (url_audio, url_audio)
        cursor.execute(query, valores)
        self.mydb.commit()
