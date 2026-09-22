# src/dominio/empleado.py
from datetime import date

class Empleado:
    def __init__(self, nombre: str, direccion: str, telefono: int, correo: str, fechainiciocontrato: date, salario: int, id= None):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fechainiciocontrato = fechainiciocontrato
        self.salario = salario

    def mostrar_datos(self) -> str:
        return f"{self.nombre} - {self.direccion} - {self.telefono} - {self.correo} - {self.fechainiciocontrato} - {self.salario}"

    def gestionar_informacion(self) -> bool:
        return True
    
    def actualizar_datos(self) -> bool:
        return self.gestionar_informacion()