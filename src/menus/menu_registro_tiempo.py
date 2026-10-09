from dominio.registro_tiempo import RegistroTiempo
from persistencia.registro_tiempo_dao import RegistroTiempoDAO
from persistencia.crear_bd import crear_tablas


def menu_registro_tiempo():
    print("\n===== ECOTECH =====")
    print("1. Registrar registro de tiempo")
    print("2. Listar registros de tiempo")
    print("3. Buscar registro de tiempo")
    print("4. Actualizar registro de tiempo")
    print("5. Eliminar registro de tiempo")
    print("0. Salir")


def ejecutar_menu():
    while True:
        menu_registro_tiempo()
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
        print(f"No fue posible registrar el registro de tiempo:")

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
        nueva_fecha = input(f"Fecha actual ({registro.fecha}), nueva fecha (YYYY-MM-DD): ").strip() or registro.fecha
        nuevas_horas = input(f"Horas actuales ({registro.cantidad_horas}), nuevas horas: ").strip()
        nueva_cantidad_horas = float(nuevas_horas) if nuevas_horas else registro.cantidad_horas
        nuevas_tareas = input(f"Tareas actuales ({registro.tareas_realizadas}), nuevas tareas: ").strip() or registro.tareas_realizadas
        nueva_descripcion = input(f"Descripción actual ({registro.descripcion}), nueva descripción: ").strip() or registro.descripcion

        registro.fecha = nueva_fecha
        registro.cantidad_horas = nueva_cantidad_horas
        registro.tareas_realizadas = nuevas_tareas
        registro.descripcion = nueva_descripcion

        try:
            RegistroTiempoDAO.actualizar(registro)
            print("Registro de tiempo actualizado correctamente.")
        except Exception as e:
            print(f"No fue posible actualizar el registro de tiempo: {e}")
    else:
        print("Registro de tiempo no encontrado.")


def eliminar_registro_tiempo():
    id_registro = input("Ingrese el ID del registro de tiempo a eliminar: ").strip()
    registro = RegistroTiempoDAO.buscar_por_id(id_registro)
    if registro:
        confirmacion = input(f"¿Está seguro de que desea eliminar el registro de fecha {registro.fecha}? (s/n): ").strip().lower()
        if confirmacion == 's':
            try:
                RegistroTiempoDAO.eliminar(id_registro)
                print("Registro de tiempo eliminado correctamente.")
            except Exception as e:
                print(f"No fue posible eliminar el registro de tiempo: {e}")
        else:
            print("Eliminación cancelada.")
    else:
        print("Registro de tiempo no encontrado.")