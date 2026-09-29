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
<<<<<<< HEAD

print("Encontrado:", encontrado.mostrar_datos())

resultado = EmpleadoDAO.eliminar(99999)
print("Resultado de eliminar empleado con ID 99999:", resultado)
print(resultado)

try:
        empleado.correo = "ana.nueva@ecotech.cl"
        actualizado = EmpleadoDAO.actualizar(empleado)

        if actualizado:
                print("Empleado actualizado correctamente.")
        else:
                print("Empleado no encontrado.")

except Exception:
        print(
                "No fue posible completar la operación."
)
=======
print("Encontrado:", encontrado.mostrar_datos())
>>>>>>> 53c835e955485d63db50440cf4d6dd47cae41487
