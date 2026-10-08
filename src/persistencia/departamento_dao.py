from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.departamento import Departamento

class DepartamentoDAO:
    @staticmethod
    def insertar(departamento):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = marcador_sql()

        sql = f"""
            INSERT INTO departamento (nombre, gerente)
            VALUES ({marcador}, {marcador})
        """

        cursor.execute(sql, (departamento.nombre, departamento.gerente))
        departamento.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return departamento
