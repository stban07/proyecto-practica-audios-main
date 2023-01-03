import MySQLdb  # pip install mysqlclient


# Conexion a base de datos mysql
class DBHelper:
    def __init__(self):

        self.mydb = MySQLdb.connect(

            host='localhost',
            user='root',
            password="",
            database="mauricio_bd",
            port=3306
        )

    bdName = 'mauricio_bd'


# se insertan los datos a la tabla Estado_animo

    def insert_metronomo(self, usuario_id, audio):
        cursor = self.mydb.cursor()
        query = "INSERT INTO mauricio_bd.app_vocalizacion(usuario_id, audio) VALUES (%s, %s)"
        valores = (str(usuario_id), audio)
        cursor.execute(query, valores)
        self.mydb.commit()

    def update_audio(self, url_audio):
        cursor = self.mydb.cursor()
        query = "UPDATE mauricio_bd.app_vocalizacion SET audio = SUBSTRING(%s, 16) WHERE audio = %s"
        valores = (url_audio, url_audio)
        cursor.execute(query, valores)
        self.mydb.commit()
