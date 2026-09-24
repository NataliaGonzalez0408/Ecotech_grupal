<<<<<<< HEAD
# persistencia/crear_bd.py
from persistencia.conexion import (abrir_conexion,obtener_motor )

=======
from persistencia.conexion import (abrir_conexion,obtener_motor )
>>>>>>> 661cb6e17ab56b25ea5a5066b1d5538b377b1b70
def crear_tablas():
    conexion = abrir_conexion()
    cursor = conexion.cursor()

    if obtener_motor() == "sqlite":
        sql = '''
<<<<<<< HEAD
            CREATE TABLE IF NOT EXISTS empleado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL
            )
'''
    else:
        sql = '''
            CREATE TABLE IF NOT EXISTS empleado (
            id INT PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(100) NOT NULL,
            correo VARCHAR(150) NOT NULL
            )   
'''
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_tablas()
    print("Base de datos preparada correctamente.")
=======
        CREATE TABLE IF NOT EXISTS empleado (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL
        )
        '''
    else:
        sql = '''
        CREATE TABLE IF NOT EXISTS empleado (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(100) NOT NULL,
        correo VARCHAR(150) NOT NULL
        )
        '''
    cursor.execute(sql)
    conexion.commit()
    conexion.close()
if __name__ == "__main__":
    crear_tablas()
    print("Base de datos preparada correctamente.")
>>>>>>> 661cb6e17ab56b25ea5a5066b1d5538b377b1b70
