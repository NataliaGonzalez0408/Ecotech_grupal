from persistencia.proyecto_dao import ProyectoDAO
from dominio.registro_tiempo import RegistroTiempo

class RegistroTiempoDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def insertar(self, registro_tiempo):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO registro_tiempo (fecha, cantidad_horas) VALUES (%s, %s)"
        cursor.execute(sql, (registro_tiempo.fecha, registro_tiempo.cantidad_horas))
        self.conexion.commit()
        cursor.close()

    def listar(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM registro_tiempo"
        cursor.execute(sql)
        registros = cursor.fetchall()
        cursor.close()
        return registros

    def buscar_por_id(self, id_registro):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM registro_tiempo WHERE id = %s"
        cursor.execute(sql, (id_registro,))
        registro = cursor.fetchone()
        cursor.close()
        return registro

