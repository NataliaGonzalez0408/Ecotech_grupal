from dominio.empleado import Empleado
class Departamento:
    def __init__(self, idDepartamento: int , nombre: str , gerente: str):
        self.idDepartamento = idDepartamento
        self.nombre = nombre
        self.gerente = gerente
        self._empleados: list[Empleado] = []

    def asignar_empleado(self,empleado):

        self.empleados.append(empleado)
        return True
    
    def reasignar_empleado(self,empleado):
        return True
    
    def editar(self, nombre,gerente):
        self.nombre = nombre
        self.gerente = gerente
        return True
    
    def eliminar(self):
        return True




def agregar_empleado(self, empleado: Empleado) -> bool:
    if empleado in self._empleados:
        return False


    self._empleados.append(empleado)
    return True
   


@property
def empleados(self) -> tuple:
    return tuple(self._empleados)


def cantidad_empleados(self) -> int:
    return len(self._empleados)








    