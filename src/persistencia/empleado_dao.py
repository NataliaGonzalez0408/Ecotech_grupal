<<<<<<< HEAD
# persistencia/empleado_dao.py
from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql
from dominio.empleado import Empleado
=======
from persistencia.conexion import abrir_conexion, obtener_motor

>>>>>>> 661cb6e17ab56b25ea5a5066b1d5538b377b1b70

class EmpleadoDAO:
    @staticmethod
    def insertar(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = "?" if obtener_motor() == "sqlite" else "%s"

        sql = f"""
<<<<<<< HEAD
            INSERT INTO empleado (nombre, correo)
            VALUES ({marcador}, {marcador})
        """

=======
        INSERT INTO empleado (nombre, correo)
        VALUES ({marcador}, {marcador})

        """
            
>>>>>>> 661cb6e17ab56b25ea5a5066b1d5538b377b1b70
        cursor.execute(sql, (empleado.nombre, empleado.correo))
        empleado.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
<<<<<<< HEAD
        return empleado

    @staticmethod
    def buscar_por_id(id_empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        marca = marcador_sql()
        sql = f"""
                SELECT id, nombre, correo
                FROM empleado WHERE id = {marca}
            """

        cursor.execute(sql, (id_empleado,))
        fila = cursor.fetchone()
        conexion.close()

        if fila is None:
            return None

        return Empleado(id=fila[0], nombre=fila[1], correo=fila[2])

    @staticmethod
    def _fila_a_empleado(fila):
        return Empleado(
            id=fila[0],
            nombre=fila[1],
            correo=fila[2]
        )
=======
        return empleado
>>>>>>> 661cb6e17ab56b25ea5a5066b1d5538b377b1b70
