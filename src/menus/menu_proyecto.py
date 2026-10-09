from dominio.proyecto import Proyecto
from persistencia.proyecto_dao import ProyectoDAO
from persistencia.crear_bd import crear_tablas

def menu_proyecto():
    print("\n===== ECOTECH =====")
    print("1. Registrar proyecto")
    print("2. Listar proyectos")
    print("3. Buscar proyecto")
    print("4. Actualizar proyecto")
    print("5. Eliminar proyecto")
    print("0. Salir")

def ejecutar_menu():
    while True:
        menu_proyecto()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_proyecto()
        elif opcion == "2":
            listar_proyectos()
        elif opcion == "3":
            buscar_proyecto()
        elif opcion == "4":
            actualizar_proyecto()
        elif opcion == "5":
            eliminar_proyecto()
        elif opcion == "0":
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta nuevamente.")

def registrar_proyecto():
    nombre_proyecto = input("Nombre del proyecto: ").strip()
    descripcion = input("Descripción del proyecto: ").strip()
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()

    proyecto = Proyecto(nombre_proyecto, descripcion, fecha_inicio)
    try:
        ProyectoDAO.insertar(proyecto)
        print("Proyecto registrado correctamente.")
    except Exception as e:
        print(f"Error al registrar el proyecto: {e}")

def listar_proyectos():
    proyectos = ProyectoDAO.listar_proyectos()
    if proyectos:
        print("\nLista de proyectos:")
        for proyecto in proyectos:
            print(f"ID: {proyecto[0]}, Nombre: {proyecto[1]}, Descripción: {proyecto[2]}, Fecha de inicio: {proyecto[3]}")
    else:
        print("No hay proyectos registrados.")

def buscar_proyecto():
    id_proyecto = input("Ingrese el ID del proyecto a buscar: ").strip()
    proyecto = ProyectoDAO.buscar_por_id(id_proyecto)
    if proyecto:
        print(f"ID: {proyecto[0]}, Nombre: {proyecto[1]}, Descripción: {proyecto[2]}, Fecha de inicio: {proyecto[3]}")
    else:
        print("Proyecto no encontrado.")

def actualizar_proyecto():
    id_proyecto = input("Ingrese el ID del proyecto a actualizar: ").strip()
    proyecto = ProyectoDAO.buscar_por_id(id_proyecto)
    if proyecto:
        print(f"ID: {proyecto[0]}, Nombre: {proyecto[1]}, Descripción: {proyecto[2]}, Fecha de inicio: {proyecto[3]}")
        nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ").strip() or proyecto[1]
        descripcion = input("Nueva descripción (dejar en blanco para no cambiar): ").strip() or proyecto[2]
        fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD) (dejar en blanco para no cambiar): ").strip() or proyecto[3]

        ProyectoDAO.actualizar_proyecto(id_proyecto, nombre, descripcion, fecha_inicio)
        print("Proyecto actualizado correctamente.")
    else:
        print("Proyecto no encontrado.")

def eliminar_proyecto():
    id_proyecto = input("Ingrese el ID del proyecto a eliminar: ").strip()
    proyecto = ProyectoDAO.buscar_por_id(id_proyecto)
    if proyecto:
        confirmacion = input(f"¿Está seguro de que desea eliminar el proyecto '{proyecto[1]}'? (s/n): ").strip().lower()
        if confirmacion == 's':
            ProyectoDAO.eliminar_proyecto(id_proyecto)
            print("Proyecto eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
    else:
        print("Proyecto no encontrado.")

def main():
    crear_tablas()
    ejecutar_menu()