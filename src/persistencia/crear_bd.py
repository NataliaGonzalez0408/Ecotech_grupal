# persistencia/crear_bd.py
from persistencia.conexion import (abrir_conexion,obtener_motor )
def crear_tablas():
    conexion = abrir_conexion()
    cursor = conexion.cursor()
    

# tabla empleado
    if obtener_motor() == "sqlite":
        sql = '''

            CREATE TABLE IF NOT EXISTS empleado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE,
            telefono TEXT,
            fecha_inicio_contrato TEXT,
            salario INTEGER
        );
'''
    else:
        sql = '''
            CREATE TABLE IF NOT EXISTS empleado (
            id INT PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(100) NOT NULL,
            correo VARCHAR(150) NOT NULL UNIQUE,
            telefono VARCHAR(20),
            fecha_inicio_contrato DATE,
            salario DECIMAL(10, 2)
        );
'''
    cursor.execute(sql)
    
#tabla departamento
    if obtener_motor() == "sqlite":
        sql = '''
        CREATE TABLE IF NOT EXISTS departamento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        gerente TEXT
        );
'''
    else:
        sql = '''
        CREATE TABLE IF NOT EXISTS departamento (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre Varchar(100) NOT NULL,
        gerente Varchar(100)
        );
'''
    cursor.execute(sql)

#tabla proyecto
    if obtener_motor() == "sqlite":
        sql = '''
        CREATE TABLE IF NOT EXISTS proyecto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        fecha_inicio TEXT
        );
'''
    else:
        sql = '''
        CREATE TABLE IF NOT EXISTS proyecto (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre Varchar(100) NOT NULL,
        descripcion Varchar(160),
        fecha_inicio Date
        );
'''
    cursor.execute(sql)

# tabla registro de tiempo
    if obtener_motor() == "sqlite":
        sql = '''
        CREATE TABLE IF NOT EXISTS registro_tiempo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        cantidad_horas REAL
        );
'''
    else:
        sql = '''
        CREATE TABLE IF NOT EXISTS registro_tiempo (
            id INT PRIMARY KEY AUTO_INCREMENT,
            fecha DATE,
            cantidad_horas DECIMAL(4, 2)
        );
'''
    cursor.execute(sql)


    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_tablas()
    print("Base de datos preparada correctamente.")

