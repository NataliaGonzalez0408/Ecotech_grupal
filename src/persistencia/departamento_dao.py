import sqlite3
from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.departamento import Departamento

class DepartamentoDAO:
    @staticmethod
    def insertar(departamento: Departamento):
        conn = abrir_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO departamentos (nombre, descripcion) VALUES (%s, %s)",
            (departamento.nombre, departamento.descripcion)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = abrir_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, descripcion FROM departamentos")
        rows = cursor.fetchall()
        conn.close()
        return [Departamento(id=row[0], nombre=row[1], descripcion=row[2]) for row in rows]

    @staticmethod
    def buscar_por_id(id_departamento):
        conn = abrir_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, nombre, descripcion FROM departamentos WHERE id = %s",
            (id_departamento,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return Departamento(id=row[0], nombre=row[1], descripcion=row[2])
        return None

    @staticmethod
    def actualizar(departamento: Departamento):
        conn = abrir_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE departamentos SET nombre = %s, descripcion = %s WHERE id = %s",
            (departamento.nombre, departamento.descripcion, departamento.id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def eliminar(id_departamento):
        conn = abrir_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM departamentos WHERE id = %s", (id_departamento,))
        conn.commit()
        conn.close()