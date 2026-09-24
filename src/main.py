#src/main.py
from dominio.empleado import Empleado
from dominio.departamento import Departamento
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.crear_bd import crear_tablas

crear_tablas()

empleado = Empleado(
        nombre="Ana Torres",
        correo="ana.torres@ecotech.cl"
)

EmpleadoDAO.insertar(empleado)

encontrado = EmpleadoDAO.buscar_por_id(empleado.id)
print("Encontrado:", encontrado.mostrar_datos())