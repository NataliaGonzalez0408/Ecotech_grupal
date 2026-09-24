# src/dominio/empleado.py
from datetime import date

class Empleado:
<<<<<<< HEAD
    #def __init__(self, nombre: str, direccion: str, telefono: int, correo: str, fechainiciocontrato: date, salario: int, id=None):

    def __init__(self, nombre: str, correo: str, id=None):
=======
    def __init__(self, nombre: str, direccion: str, telefono: int, correo: str, fechainiciocontrato: date, salario: int, id= None):
        self.id = id
>>>>>>> 661cb6e17ab56b25ea5a5066b1d5538b377b1b70
        self.nombre = nombre
        #self.direccion = direccion
        #self.telefono = telefono
        self.correo = correo
        #self.fechainiciocontrato = fechainiciocontrato
        #self.salario = salario
        self.id = id

    def mostrar_datos(self) -> str:
        #return f"{self.nombre} - {self.direccion} - {self.telefono} - {self.correo} - {self.fechainiciocontrato} - {self.salario} - {self.id}"
        
        return f"{self.nombre} - {self.correo} - {self.id}"

    def gestionar_informacion(self) -> bool:
        return True
    
    def actualizar_datos(self) -> bool:
        return self.gestionar_informacion()