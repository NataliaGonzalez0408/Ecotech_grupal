import sqlite3
from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.proyecto import Proyecto

class ProyectoDAO:
    @staticmethod
    def insertar(proyecto):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = marcador_sql()

        sql = f"""
            INSERT INTO proyecto (nombre, descripcion, fecha_inicio)
            VALUES ({marcador}, {marcador}, {marcador})
        """

        cursor.execute(sql, (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio))
        proyecto.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return proyecto
        
    @staticmethod
    def crear_proyecto(self, proyecto):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO proyecto (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
        cursor.execute(sql, (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio))
        self.conexion.commit()
        cursor.close()
        return proyecto
    
    @staticmethod
    def listar_proyectos():
        conn = abrir_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, descripcion, fecha_inicio FROM proyectos")
        proyectos = cursor.fetchall()
        conn.close()
        return proyectos

    @staticmethod
    def obtener_proyectos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM proyecto"
        cursor.execute(sql)
        proyectos = cursor.fetchall()
        cursor.close()
        return proyectos

    @staticmethod
    def buscar_por_id(id_proyecto):
        conn = abrir_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM proyectos WHERE id = %s",
            (id_proyecto,)
        )
        proyecto = cursor.fetchone()
        conn.close()
        return proyecto

    @staticmethod
    def actualizar_proyecto(id_proyecto, nombre, descripcion, fecha_inicio):
        conn = abrir_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE proyectos SET nombre = %s, descripcion = %s, fecha_inicio = %s WHERE id = %s",
            (nombre, descripcion, fecha_inicio, id_proyecto)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def eliminar_proyecto(id_proyecto):
        conn = abrir_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM proyectos WHERE id = %s", (id_proyecto,))
        conn.commit()
        conn.close()