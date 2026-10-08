from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.crear_bd import crear_tablas

def mostrar_menu():
        print("\n===== ECOTECH =====")
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("3. Buscar empleado")
        print("4. Actualizar empleado")
        print("5. Eliminar empleado")
        print("0. Salir")

def ejecutar_menu():
        while True:
                mostrar_menu()
                opcion = input("Selecciona una opción: ")

                if opcion == "1":
                        registrar_empleado()
                elif opcion == "2":
                        listar_empleados()
                elif opcion == "3":
                        buscar_empleado()
                elif opcion == "4":
                        actualizar_empleado()
                elif opcion == "5":
                        eliminar_empleado()
                elif opcion == "0":
                        print("Saliendo del sistema... ¡Hasta luego!")
                        break
                else:
                        print("Opción inválida, intenta nuevamente.")

def registrar_empleado():
        nombre = input("Nombre: ").strip()
        correo = input("Correo: ").strip()
        telefono = input("Teléfono: ").strip()
        fecha_inicio_contrato = input("Fecha de inicio de contrato (YYYY-MM-DD): ").strip()
        salario = float(input("Salario: ").strip())

        empleado = Empleado(nombre, correo,telefono)
        try:
                EmpleadoDAO.insertar(empleado)
                print("Empleado registrado correctamente.")

        except Exception:
                print("No fue posible registrar el empleado.")

def listar_empleados():
        empleados = EmpleadoDAO.listar()
        if empleados:
                print("\nLista de empleados:")
                for empleado in empleados:
                        print(f"ID: {empleado.id}, Nombre: {empleado.nombre}, Correo: {empleado.correo}, Teléfono: {empleado.telefono}")
        else:
                print("No hay empleados registrados.")

def buscar_empleado():
        id_empleado = input("Ingrese el ID del empleado a buscar: ").strip()
        empleado = EmpleadoDAO.buscar_por_id(id_empleado)
        if empleado:
                print(f"ID: {empleado.id}, Nombre: {empleado.nombre}, Correo: {empleado.correo}, Teléfono: {empleado.telefono}")
        else:
                print("Empleado no encontrado.")

def actualizar_empleado():
        id_empleado = input("Ingrese el ID del empleado a actualizar: ").strip()
        empleado = EmpleadoDAO.buscar_por_id(id_empleado)
        if empleado:
                nombre = input(f"Nombre ({empleado.nombre}): ").strip() or empleado.nombre
                correo = input(f"Correo ({empleado.correo}): ").strip() or empleado.correo
                telefono = input(f"Teléfono ({empleado.telefono}): ").strip() or empleado.telefono

                empleado.nombre = nombre
                empleado.correo = correo
                empleado.telefono = telefono

                try:
                        EmpleadoDAO.actualizar(empleado)
                        print("Empleado actualizado correctamente.")
                except Exception:
                        print("No fue posible actualizar el empleado.")
        else:
                print("Empleado no encontrado.")

def eliminar_empleado():
        id_empleado = input("Ingrese el ID del empleado a eliminar: ").strip()
        empleado = EmpleadoDAO.buscar_por_id(id_empleado)
        if empleado:
                confirmacion = input(f"¿Está seguro de que desea eliminar al empleado {empleado.nombre}? (s/n): ").strip().lower()
                if confirmacion == 's':
                        try:
                                EmpleadoDAO.eliminar(empleado)
                                print("Empleado eliminado correctamente.")
                        except Exception:
                                print("No fue posible eliminar el empleado.")
                else:
                        print("Eliminación cancelada.")
        else:
                print("Empleado no encontrado.")

def main():
        crear_tablas()
        ejecutar_menu()