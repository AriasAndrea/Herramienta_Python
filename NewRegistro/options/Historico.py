import tkinter 
import datetime
import pandas as pd
import sys
sys.path.insert(0, 'gestores/GestorRegistro.py')
sys.path.insert(0, 'gestores/GestorModRegistro.py')


class Historico:
    def __init__(self):
        self.nombre_archivo = "historico.xlsx"  # Nombre del archivo Excel
        self.registros = []

    def addRegistro(self, datos):
        try:
            # Cargar el archivo Excel existente
            df = pd.read_excel(self.nombre_archivo)
        except FileNotFoundError:
            # Crear un nuevo DataFrame si el archivo no existe
            df = pd.DataFrame(columns=["Número de PETSIS", "Tipo de Entorno Origen", "Tipo de Entorno Destino",
                                       "Nombre Servicio", "Nombre Aplicación", "Autorizado desde",
                                       "Tipo Conexión : Puerto", "Descripción", "Nombre Regla_FW"])

        # Obtener el índice del último registro guardado
        index = df.index[-1] + 1 if not df.empty else 0

        # Agregar el índice al inicio del registro
        datos.insert(0, index + 1)

        # Agregar el registro al DataFrame
        df.loc[len(df)] = datos

        # Guardar el DataFrame en el archivo Excel
        df.to_excel(self.nombre_archivo, index=False)

    def actualizar_excel(self):
        # Obtener la fecha actual
        fecha_actual = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # Crear una copia de seguridad con la fecha en el nombre del archivo
        nombre_archivo_backup = f"historico_{fecha_actual}.xlsx"
        df_backup = pd.DataFrame(self.registros)
        df_backup.to_excel(nombre_archivo_backup, index=False)
        print(f"Copia de seguridad creada: {nombre_archivo_backup}")

        # Leer el archivo actual (si existe)
        try:
            df_actual = pd.read_excel("historico.xlsx")
        except FileNotFoundError:
            df_actual = pd.DataFrame()

        # Concatenar los registros nuevos con los registros existentes
        df_nuevo = pd.DataFrame(self.registros)
        df_actual = pd.concat([df_actual, df_nuevo], ignore_index=True)

        # Eliminar registros duplicados (si existen)
        df_actual.drop_duplicates(inplace=True)

        # Guardar el archivo actualizado
        df_actual.to_excel("historico.xlsx", index=False)
        print("Archivo actualizado: historico.xlsx")
