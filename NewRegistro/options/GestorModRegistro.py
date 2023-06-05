import tkinter as tk
import sys
sys.path.insert(0, 'options/Historico.py')

from options.Historico import Historico

class GestorModRegistro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Editar Registro")
        self.numero_petsis = ""
        self.tipo_entorno_origen = ""
        self.tipo_entorno_destino = ""
        self.nombre_servicio = ""
        self.nombre_aplicacion = ""
        self.autorizado_desde = ""
        self.tipo_conexion_puerto = ""
        self.descripcion = ""
        self.nombre_regla_fw = ""

        buscar_button = tk.Button(self.root, text="Buscar Registro", command=self.search_registro)
        buscar_button.pack()

        menu_principal_button = tk.Button(self.root, text="Menú principal", command=self.volver_menu_principal)
        menu_principal_button.pack()
    

    def search_registro(self):
        # Obtener los valores ingresados en los campos
        self.numero_petsis = self.numero_petsis_entry.get()
        self.tipo_entorno_origen = self.tipo_entorno_origen_entry.get()
        self.tipo_entorno_destino = self.tipo_entorno_destino_entry.get()
        self.nombre_servicio = self.nombre_servicio_entry.get()
        self.nombre_aplicacion = self.nombre_aplicacion_entry.get()
        self.tipo_conexion_puerto = self.tipo_conexion_puerto_entry.get()
        self.descripcion = self.descripcion_entry.get()
        self.nombre_regla_fw = self.nombre_regla_fw_entry.get()

        # Realizar la búsqueda del registro en el histórico
        historico = Historico()
        resultado = historico.searchRegistro(self.numero_petsis, self.tipo_entorno_origen, self.tipo_entorno_destino,
                                             self.nombre_servicio, self.nombre_aplicacion, self.tipo_conexion_puerto,
                                             self.descripcion, self.nombre_regla_fw)
        # Mostrar el resultado de la búsqueda
        self.mostrar_resultados(resultado)
    
        def mostrar_resultados(self, resultados):
            if len(resultados) == 0:
               print("No se han encontrado coincidencias")
            else:
                # Crear una tabla para mostrar los resultados
                table_frame = tk.Frame(self.root)
                table_frame.pack()
            # Crear las cabeceras de la tabla
            cabeceras = ["Número de PETSIS", "Tipo de Entorno Origen", "Tipo de Entorno Destino", "Nombre Servicio",
                         "Nombre Aplicación", "Autorizado desde", "Tipo Conexión : Puerto", "Descripción",
                         "Nombre Regla_FW"]
            for i, cabecera in enumerate(cabeceras):
                header_label = tk.Label(table_frame, text=cabecera, relief=tk.RIDGE)
                header_label.grid(row=0, column=i, sticky=tk.NSEW)
            # Mostrar los registros en la tabla
            for i, registro in enumerate(resultados):
                for j, valor in enumerate(registro):
                    cell_label = tk.Label(table_frame, text=valor, relief=tk.RIDGE)
                    cell_label.grid(row=i + 1, column=j, sticky=tk.NSEW)
                # Agregar botones para editar y borrar el registro
                editar_button = tk.Button(table_frame, text="Editar Registro",
                                          command=lambda row=i: self.editar_registro(resultados[row]))
                editar_button.grid(row=i + 1, column=len(cabeceras), sticky=tk.NSEW)

                borrar_button = tk.Button(table_frame, text="Borrar Registro",
                                          command=lambda row=i: self.borrar_registro(resultados[row]))
                borrar_button.grid(row=i + 1, column=len(cabeceras) + 1, sticky=tk.NSEW)
        
            def editar_registro(self, registro):
                # Crear una nueva ventana de edición con los campos y valores del registro seleccionado
                editar_window = tk.Toplevel(self.root)
                editar_window.title("Editar Registro")
                # Crear los campos de edición
                numero_petsis_label = tk.Label(editar_window, text="Número de PETSIS:")
                numero_petsis_label.pack()
                numero_petsis_entry = tk.Entry(editar_window)
                numero_petsis_entry.insert(tk.END, registro[0])
                numero_petsis_entry.pack()

                tipo_entorno_origen_label = tk.Label(editar_window, text="Tipo de Entorno Origen:")
                tipo_entorno_origen_label.pack()
                tipo_entorno_origen_entry = tk.Entry(editar_window)
                tipo_entorno_origen_entry.insert(tk.END, registro[1])
                tipo_entorno_origen_entry.pack()

                tipo_entorno_destino_label = tk.Label(editar_window, text="Tipo de Entorno Destino:")
                tipo_entorno_destino_label.pack()
                tipo_entorno_destino_entry = tk.Entry(editar_window)
                tipo_entorno_destino_entry.insert(tk.END, registro[2])
                tipo_entorno_destino_entry.pack()

                nombre_servicio_label = tk.Label(editar_window, text="Nombre Servicio:")
                nombre_servicio_label.pack()
                nombre_servicio_entry = tk.Entry(editar_window)
                nombre_servicio_entry.insert(tk.END, registro[3])
                nombre_servicio_entry.pack()

                nombre_aplicacion_label = tk.Label(editar_window, text="Nombre Aplicación:")
                nombre_aplicacion_label.pack()
                nombre_aplicacion_entry = tk.Entry(editar_window)
                nombre_aplicacion_entry.insert(tk.END, registro[4])
                nombre_aplicacion_entry.pack()

                autorizado_desde_label = tk.Label(editar_window, text="Autorizado desde:")
                autorizado_desde_label.pack()
                autorizado_desde_entry = tk.Entry(editar_window)
                autorizado_desde_entry.insert(tk.END, registro[5])
                autorizado_desde_entry.pack()

                tipo_conexion_puerto_label = tk.Label(editar_window, text="Tipo Conexión : Puerto:")
                tipo_conexion_puerto_label.pack()
                tipo_conexion_puerto_entry = tk.Entry(editar_window)
                tipo_conexion_puerto_entry.insert(tk.END, registro[6])
                tipo_conexion_puerto_entry.pack()

                descripcion_label = tk.Label(editar_window, text="Descripción:")
                descripcion_label.pack()
                descripcion_entry = tk.Entry(editar_window)
                descripcion_entry.insert(tk.END, registro[7])
                descripcion_entry.pack()

                nombre_regla_fw_label = tk.Label(editar_window, text="Nombre Regla_FW:")
                nombre_regla_fw_label.pack()
                nombre_regla_fw_entry = tk.Entry(editar_window)
                nombre_regla_fw_entry.insert(tk.END, registro[8])
                nombre_regla_fw_entry.pack()

                # Agregar un botón para guardar los cambios
                guardar_button = tk.Button(editar_window, text="Guardar Cambios",
                                    command=lambda: self.guardar_cambios(registro, numero_petsis_entry.get(),
                                                                        tipo_entorno_origen_entry.get(),
                                                                        tipo_entorno_destino_entry.get(),
                                                                        nombre_servicio_entry.get(),
                                                                        nombre_aplicacion_entry.get(),
                                                                        autorizado_desde_entry.get(),
                                                                        tipo_conexion_puerto_entry.get(),
                                                                        descripcion_entry.get(),
                                                                        nombre_regla_fw_entry.get(),
                                                                        editar_window))
                guardar_button.pack()
            
            def guardar_cambios(self, registro, numero_petsis, tipo_entorno_origen, tipo_entorno_destino, nombre_servicio,
                        nombre_aplicacion, autorizado_desde, tipo_conexion_puerto, descripcion, nombre_regla_fw,
                        editar_window):
                # Realizar los cambios en el registro
                registro[0] = numero_petsis
                registro[1] = tipo_entorno_origen
                registro[2] = tipo_entorno_destino
                registro[3] = nombre_servicio
                registro[4] = nombre_aplicacion
                registro[5] = autorizado_desde
                registro[6] = tipo_conexion_puerto
                registro[7] = descripcion
                registro[8] = nombre_regla_fw
                # Guardar los cambios en el histórico (puedes ajustar este método según tu implementación)
                historico = Historico()
                historico.guardarCambios()
                # Cerrar la ventana de edición
                editar_window.destroy()
            def borrar_registro(self, registro):
                # Eliminar el registro del histórico (puedes ajustar este método según tu implementación)
                historico = Historico()
                historico.eliminarRegistro(registro)
                # Actualizar la tabla de resultados
                self.search_registro()
    
    def volver_menu_principal(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gestor = GestorModRegistro()
    gestor.run()
