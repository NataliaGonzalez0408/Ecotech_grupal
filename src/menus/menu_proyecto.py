from dominio.proyecto import Proyecto
from persistencia.proyecto_dao import proyectoDAO
from persistencia.conexion import abrir_conexion
from persistencia.crear_bd import crear_tablas

def mostrar_menu():
        print("\n===== ECOTECH =====")
        print("1. Registrar proyectos")
        print("2. Listar proyectos")
        print("3. Buscar proyectos")
        print("4. Actualizar proyectos")
        print("5. Eliminar proyectos")
        print("0. Salir")

def ejecutar_menu():
        while True:
                mostrar_menu()
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
    proyectoDAO.insertar(proyecto)
    print("Proyecto registrado correctamente.")
except Exception:
    print(f"Error al registrar el proyecto.")

def listar_proyectos():
    proyectos = ProyectoDAO.listar_proyectos()
    for proyecto in proyectos:
        print(f"ID: {proyecto[0]}, Nombre: {proyecto[1]}, Descripción: {proyecto[2]}, Fecha de inicio: {proyecto[3]}")

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
        nombre = input("Nuevo nombre del proyecto (dejar en blanco para no cambiar): ").strip()
        descripcion = input("Nueva descripción del proyecto (dejar en blanco para no cambiar): ").strip()
        fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD) (dejar en blanco para no cambiar): ").strip()
        ProyectoDAO.actualizar_proyecto(id_proyecto, nombre, descripcion, fecha_inicio)

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