from dominio.departamento import Departamento
from persistencia.departamento_dao import DepartamentoDAO
from persistencia.crear_bd import crear_tablas

def mostrar_menu():
        print("\n===== ECOTECH =====")
        print("1. Registrar departamentos")
        print("2. Listar departamentos")
        print("3. Buscar departamentos")
        print("4. Actualizar departamentos")
        print("5. Eliminar departamentos")
        print("0. Salir")

def ejecutar_menu():
        while True:
                mostrar_menu()
                opcion = input("Selecciona una opción: ")

                if opcion == "1":
                        registrar_departamento()
                elif opcion == "2":
                        listar_departamentos()
                elif opcion == "3":
                        buscar_departamento()
                elif opcion == "4":
                        actualizar_departamento()
                elif opcion == "5":
                        eliminar_departamento()
                elif opcion == "0":
                        print("Saliendo del sistema... ¡Hasta luego!")
                        break
                else:
                        print("Opción inválida, intenta nuevamente.")

def registrar_departamento():
        nombre = input("Nombre del departamento: ").strip()
        descripcion = input("Descripción del departamento: ").strip()

        departamento = Departamento(nombre, descripcion)
        try:
                DepartamentoDAO.insertar(departamento)
                print("Departamento registrado correctamente.")
        except Exception:
                print("No fue posible registrar el departamento.")

def listar_departamentos():
        departamentos = DepartamentoDAO.listar()
        if departamentos:
                print("\nLista de departamentos:")
                for departamento in departamentos:
                        print(f"ID: {departamento.id}, Nombre: {departamento.nombre}, Descripción: {departamento.descripcion}")
        else:
                print("No hay departamentos registrados.")

def buscar_departamento():
        id_departamento = input("Ingrese el ID del departamento a buscar: ").strip()
        departamento = DepartamentoDAO.buscar_por_id(id_departamento)
        if departamento:
                print(f"ID: {departamento.id}, Nombre: {departamento.nombre}, Descripción: {departamento.descripcion}")
        else:
                print("Departamento no encontrado.")

def actualizar_departamento():
        id_departamento = input("Ingrese el ID del departamento a actualizar: ").strip()
        departamento = DepartamentoDAO.buscar_por_id(id_departamento)
        if departamento:
                nombre = input(f"Nuevo nombre (actual: {departamento.nombre}): ").strip()
                descripcion = input(f"Nueva descripción (actual: {departamento.descripcion}): ").strip()

                departamento.nombre = nombre if nombre else departamento.nombre
                departamento.descripcion = descripcion if descripcion else departamento.descripcion

                try:
                        DepartamentoDAO.actualizar(departamento)
                        print("Departamento actualizado correctamente.")
                except Exception:
                        print("No fue posible actualizar el departamento.")
        else:
                print("Departamento no encontrado.")

def eliminar_departamento():
        id_departamento = input("Ingrese el ID del departamento a eliminar: ").strip()
        departamento = DepartamentoDAO.buscar_por_id(id_departamento)
        if departamento:
                try:
                        DepartamentoDAO.eliminar(id_departamento)
                        print("Departamento eliminado correctamente.")
                except Exception:
                        print("No fue posible eliminar el departamento.")
        else:
                print("Departamento no encontrado.")

def main():
        crear_tablas()
        ejecutar_menu()