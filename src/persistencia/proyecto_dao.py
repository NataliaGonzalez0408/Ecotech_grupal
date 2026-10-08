from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.proyecto import Proyecto


class proyectoDAO:
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

    @staticmethod
    def obtener_proyectos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM proyecto"
        cursor.execute(sql)
        proyectos = cursor.fetchall()
        cursor.close()
        return proyectos

    @staticmethod
    def buscar_por_id(self, id_proyecto):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM proyecto WHERE id = %s"
        cursor.execute(sql, (id_proyecto,))
        proyecto = cursor.fetchone()
        cursor.close()
        return proyecto

    @staticmethod
    def actualizar_proyecto(self, id_proyecto, nombre, descripcion, fecha_inicio):
        cursor = self.conexion.cursor()
        sql = "UPDATE proyecto SET nombre = %s, descripcion = %s, fecha_inicio = %s WHERE id = %s"
        cursor.execute(sql, (nombre, descripcion, fecha_inicio, id_proyecto))
        self.conexion.commit()
        cursor.close()

    @staticmethod
    def eliminar_proyecto(self, id_proyecto):
        cursor = self.conexion.cursor()
        sql = "DELETE FROM proyecto WHERE id = %s"
        cursor.execute(sql, (id_proyecto,))
        self.conexion.commit()
        cursor.close()