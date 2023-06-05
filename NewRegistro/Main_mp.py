import sys
sys.path.insert(0, 'options/Historico.py')
sys.path.insert(0, 'options/GestorRegistro.py')
sys.path.insert(0, 'options/GestorModRegistro.py')

import GestorModRegistro
from ./options/GestorRegistro import GestorRegistro

class MenuPrincipal:
    def __init__(self):
       from options.Historico import Historico
       self.historico = Historico()  # Instancia de la clase Historico

    def mostrar_menu(self):
        opcion = 0

        while opcion != 4:
            print("---- MENÚ ----")
            print("1. Nuevo Registro")
            print("2. Editar Registro")
            print("3. Actualizar Excel")
            print("4. Salir")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                print("Opción seleccionada: Nuevo Registro")

                gestor_registros = GestorRegistro()
                gestor_registros.ingresar_registro()
                datos_registro = gestor_registros.obtener_datos_registro()
                self.historico.addRegistro(datos_registro)
                # Aquí iría el código adicional para la opción "Nuevo Registro"
            elif opcion == 2:
                print("Opción seleccionada: Editar Registro")
                gestor_mod_registros = GestorModRegistro()
                gestor_mod_registros.mostrar_menu()
            elif opcion == 3:
                print("Opción seleccionada: Actualizar Excel")
                # Aquí iría el código para la opción "Actualizar Excel"
                self.historico.actualizar_excel()
            elif opcion == 4:
                print("Saliendo del programa...")
            else:
                print("Opción inválida. Intente nuevamente.")
# Crear una instancia de la clase MenuPrincipal y mostrar el menú
menu = MenuPrincipal()
menu.mostrar_menu()
