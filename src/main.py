#src/main.py
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.crear_bd import crear_tablas
from menus.menu_empleado import menu_empleado
from menus.menu_proyecto import menu_proyecto
from menus.menu_departamento import menu_departamento
from menus.menu_registro_tiempo import menu_registro_tiempo

def main():
        while True:
                print("\n=== SISTEMA ===")
                print("1. Empleados")
                print("2. Proyectos")
                print("3. Departamentos")
                print("4. Registros de Tiempo")
                print("0. Salir")

                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                        menu_empleado()
                elif opcion == "2":
                        menu_proyecto()
                elif opcion == "3":
                        menu_departamento()
                elif opcion == "4":
                        menu_registro_tiempo()
                elif opcion == "0":
                        break
                else:
                        print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
        crear_tablas()
        main()