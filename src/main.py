#src/main.py
from dominio.empleado import Empleado
from dominio.departamento import Departamento

empleado_ana = Empleado(
        nombre="Ana Torres",
        correo="ana.torres@ecotech.cl"
)

empleado_juanito = Empleado(
        nombre="Juanito Pérez",
        correo="juanito.pérez@ecotech.cl"
)

dpt_desarrollo = Departamento("dpt Desarrollo")

dpt_desarrollo.agregar_empleado(empleado_ana)
dpt_desarrollo.agregar_empleado(empleado_juanito)

print(dpt_desarrollo.cantidad_empleados())

for empleado in dpt_desarrollo.empleados:
        print(empleado.mostrar_datos())