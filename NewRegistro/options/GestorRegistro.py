import datetime
import tkinter as tk
import sys
sys.path.insert(0, 'options/Historico.py')
sys.path.insert(0, './libraries/transformaciones.py')

from options.Historico import Historico
from libraries import Transformaciones


class GestorRegistros:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestor de Registros")
        self.numero_petsis = ""
        self.tipo_entorno_origen = ""
        self.tipo_entorno_destino = ""
        self.nombre_servicio = ""
        self.nombre_aplicacion = ""
        self.autorizado_desde = ""
        self.tipo_conexion_puerto = ""
        self.descripcion = ""

        menu_principal_button = tk.Button(self.root, text="Menú principal", command=self.volver_menu_principal)
        menu_principal_button.pack()

    def ingresar_registro(self):
        print("---- Nuevo Registro ----")

        self.numero_petsis = input("Número de PETSIS (obligatorio): ")

        # Validar que el número de PETSIS no esté en blanco
        while self.numero_petsis.strip() == "":
            print("El número de PETSIS es obligatorio. Intente nuevamente.")
            self.numero_petsis = input("Número de PETSIS (obligatorio): ")

        print("Tipo de Entorno Origen:")
        self.tipo_entorno_origen = self.seleccionar_entorno()

        print("Tipo de Entorno Destino:")
        self.tipo_entorno_destino = self.seleccionar_entorno()

        self.nombre_servicio = input("Nombre Servicio: ")
        self.nombre_aplicacion = input("Nombre Aplicación: ")
        self.autorizado_desde = self.validar_fecha("Autorizado desde (dd/mm/aaaa): ")
        self.tipo_conexion_puerto = input("Tipo Conexión : Puerto: ")
        self.descripcion = input("Descripción: ")
        

        print("\nRegistro ingresado exitosamente:")
        print("Número de PETSIS:", self.numero_petsis)
        print("Tipo de Entorno Origen:", self.tipo_entorno_origen)
        print("Tipo de Entorno Destino:", self.tipo_entorno_destino)
        print("Nombre Servicio:", self.nombre_servicio)
        print("Nombre Aplicación:", self.nombre_aplicacion)
        print("Autorizado desde:", self.autorizado_desde)
        print("Tipo Conexión : Puerto:", self.tipo_conexion_puerto)
        print("Descripción:", self.descripcion)

        self.obtener_datos_registro()

    def seleccionar_entorno(self):
        entornos = ["desarrollo", "Test", "integración", "aceptación", "producción", "servicio comunes", "user"]

        print("Seleccione una opción:")
        for i, entorno in enumerate(entornos):
            print(f"{i+1}. {entorno}")

        opcion = int(input("Ingrese el número de la opción seleccionada: "))

        # Validar la opción ingresada
        while opcion < 1 or opcion > len(entornos):
            print("Opción inválida. Intente nuevamente.")
            opcion = int(input("Ingrese el número de la opción seleccionada: "))

        return entornos[opcion - 1]

    def validar_fecha(self, mensaje):
        fecha = input(mensaje)
        formato_fecha = "%d/%m/%Y"

        # Validar el formato de fecha
        try:
            fecha_valida = datetime.datetime.strptime(fecha, formato_fecha)
            return fecha_valida.strftime(formato_fecha)
        except ValueError:
            print("Fecha inválida. Intente nuevamente.")
            return self.validar_fecha(mensaje)
   
        
    def new_nombre(self):
        tipo_entorno_origen = self.tipo_entorno_origen.get()  # Obtener el valor seleccionado del campo
        tipo_entorno_destino = self.tipo_entorno_destino.get()  # Obtener el valor seleccionado del campo
        nombre_servicio = self.nombre_servicio.get()
        nombre_aplicacion = self.nombre_aplicacion.get()

        # Realiza las transformaciones para obtener el nombre de la regla_fw
        tipo_entorno_origen_transformado = Transformaciones.transformar_tipo_entorno(tipo_entorno_origen)
        tipo_entorno_destino_transformado = Transformaciones.transformar_tipo_entorno(tipo_entorno_destino)
        # Elimina los espacios en blanco y concatena los campos de Nombre Servicio y Nombre Aplicación
        nombre_servicio = nombre_servicio.replace(" ", "")
        nombre_aplicacion = nombre_aplicacion.replace(" ", "")
        nombre_regla_fw = tipo_entorno_origen_transformado + tipo_entorno_destino_transformado + nombre_servicio + "-" + nombre_aplicacion

        # Muestra el resultado en el campo "Nombre Regla_FW"
        print("Nombre Regla_FW:", nombre_regla_fw)

        # Muestra el resultado en el campo "Nombre Regla_FW"
        self.nombre_regla_fw_entry.delete(0, tk.END)
        self.nombre_regla_fw_entry.insert(0, nombre_regla_fw)
        # Mostrar los datos en el campo "Nombre Regla_FW"
        self.new_nombre()

    def volver_menu_principal(self):
        self.root.destroy()

def obtener_datos_registro(self):
    numero_petsis = self.numero_petsis
    tipo_entorno_origen = self.tipo_entorno_origen
    tipo_entorno_destino = self.tipo_entorno_destino
    nombre_servicio = self.nombre_servicio
    nombre_aplicacion = self.nombre_aplicacion
    autorizado_desde = self.autorizado_desde
    tipo_conexion_puerto = self.tipo_conexion_puerto
    descripcion = self.descripcion
    nombre_regla_fw = self.nombre_regla_fw

    # Aquí puedes realizar la lógica de actualizar el registro en el historico
    # Almacena los datos recopilados en una variable
    datos = {
        "numero_petsis": numero_petsis,
        "tipo_entorno_origen": tipo_entorno_origen,
        "tipo_entorno_destino": tipo_entorno_destino,
        "nombre_servicio": nombre_servicio,
        "nombre_aplicacion": nombre_aplicacion,
        "autorizado_desde": autorizado_desde,
        "tipo_conexion_puerto": tipo_conexion_puerto,
        "descripcion": descripcion,
        "nombre_regla_fw": nombre_regla_fw
    }
