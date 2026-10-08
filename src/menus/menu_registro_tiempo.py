from dominio.registro_tiempo import RegistroTiempo
from persistencia.registro_tiempo_dao import RegistroTiempoDAO
from persistencia.conexion import abrir_conexion
from persistencia.crear_bd import crear_tablas

abrir_conexion()
crear_tablas()

def mostrar_menu():
        print("\n===== ECOTECH =====")
        print("1. Registrar registros de tiempo")
        print("2. Listar registros de tiempo")
        print("3. Buscar registro de tiempo")
        print("4. Actualizar registro de tiempo")
        print("5. Eliminar registro de tiempo")
        print("0. Salir")

def ejecutar_menu():
        while True:
                mostrar_menu()
                opcion = input("Selecciona una opción: ")

                if opcion == "1":
                        registrar_registro_tiempo()
                elif opcion == "2":
                        listar_registros_tiempo()
                elif opcion == "3":
                        buscar_registro_tiempo()
                elif opcion == "4":
                        actualizar_registro_tiempo()
                elif opcion == "5":
                        eliminar_registro_tiempo()
                elif opcion == "0":
                        print("Saliendo del sistema... ¡Hasta luego!")
                        break
                else:
                        print("Opción inválida, intenta nuevamente.")

def registrar_registro_tiempo():
    fecha = input("Fecha (YYYY-MM-DD): ").strip()
    cantidad_horas = float(input("Cantidad de horas: ").strip())
    tareas_realizadas = input("Tareas realizadas: ").strip()
    descripcion = input("Descripción: ").strip()

registro_tiempo = RegistroTiempo(fecha, cantidad_horas, tareas_realizadas, descripcion)
try:
    RegistroTiempoDAO.insertar(registro_tiempo)
    print("Registro de tiempo registrado correctamente.")
except Exception:
    print("No fue posible registrar el registro de tiempo.")

def listar_registros_tiempo():
    registros = RegistroTiempoDAO.listar()
    if registros:
        print("\nLista de registros de tiempo:")
        for reg in registros:
            print(f"ID: {reg.id}, Fecha: {reg.fecha}, Horas: {reg.cantidad_horas}")
    else:
        print("No hay registros de tiempo registrados.")

def buscar_registro_tiempo():
    id_registro = input("Ingrese el ID del registro de tiempo a buscar: ").strip()
    registro = RegistroTiempoDAO.buscar_por_id(id_registro)
    if registro:
        print(f"ID: {registro.id}, Fecha: {registro.fecha}, Horas: {registro.cantidad_horas}")
    else:
        print("Registro de tiempo no encontrado.")

def actualizar_registro_tiempo():
    id_registro = input("Ingrese el ID del registro de tiempo a actualizar: ").strip()
    registro = RegistroTiempoDAO.buscar_por_id(id_registro)
    if registro:
        nueva_fecha = input(f"Fecha actual ({registro.fecha}), nueva fecha (YYYY-MM-DD): ").strip()
        nueva_cantidad_horas = float(input(f"Horas actuales ({registro.cantidad_horas}), nuevas horas: ").strip())
        nuevas_tareas_realizadas = input(f"Tareas actuales ({registro.tareas_realizadas}), nuevas tareas: ").strip()
        nueva_descripcion = input(f"Descripción actual ({registro.descripcion}), nueva descripción: ").strip()

        registro.fecha = nueva_fecha if nueva_fecha else registro.fecha
        registro.cantidad_horas = nueva_cantidad_horas if nueva_cantidad_horas else registro.cantidad_horas
        registro.tareas_realizadas = nuevas_tareas_realizadas if nuevas_tareas_realizadas else registro.tareas_realizadas
        registro.descripcion = nueva_descripcion if nueva_descripcion else registro.descripcion

        try:
            RegistroTiempoDAO.actualizar(registro)
            print("Registro de tiempo actualizado correctamente.")
        except Exception:
            print("No fue posible actualizar el registro de tiempo.")
    else:
        print("Registro de tiempo no encontrado.")


def eliminar_registro_tiempo():
    id_registro = input("Ingrese el ID del registro de tiempo a eliminar: ").strip()
    registro = RegistroTiempoDAO.buscar_por_id(id_registro)
    if registro:
        try:
            RegistroTiempoDAO.eliminar(id_registro)
            print("Registro de tiempo eliminado correctamente.")
        except Exception:
            print("No fue posible eliminar el registro de tiempo.")
    else:
        print("Registro de tiempo no encontrado.")