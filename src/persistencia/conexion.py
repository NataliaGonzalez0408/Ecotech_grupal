<<<<<<< HEAD
# persistencia/conexion.py
=======
>>>>>>> 661cb6e17ab56b25ea5a5066b1d5538b377b1b70
import os
import sqlite3
import pymysql
from dotenv import load_dotenv
<<<<<<< HEAD

=======
>>>>>>> 661cb6e17ab56b25ea5a5066b1d5538b377b1b70
load_dotenv()

def obtener_motor():
    return os.getenv("DB_ENGINE", "sqlite").lower()
<<<<<<< HEAD

def abrir_conexion():
    motor = obtener_motor()

    if motor == "sqlite":
        return sqlite3.connect(os.getenv("DB_NAME", "ecotech.db"))

    if motor == "mysql":
        return pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            charset="utf8mb4",
            )
    raise ValueError(f"Motor no soportado: {motor}")

def marcador_sql():
    if obtener_motor() == "sqlite":
        return "?"
    return "%s"
=======
def abrir_conexion():
    motor = obtener_motor()
    if motor == "sqlite":
        return sqlite3.connect(os.getenv("DB_NAME", "ecotech.db"))
    if motor == "mysql":
        return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        charset="utf8mb4",
        )
    raise ValueError(f"Motor no soportado: {motor}")
>>>>>>> 661cb6e17ab56b25ea5a5066b1d5538b377b1b70
