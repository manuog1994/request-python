import tkinter as tk
import requests

def obtener_datos():
    # Realizar una solicitud a la API
    url = 'URL de la API'
    response = requests.get(url)

    if response.status_code == 200:
        # Parsear los datos JSON (ajusta esto según la estructura de la API)
        datos = response.json()

        # Limpiar la lista existente
        lista.delete(0, tk.END)

        # Entrar en json y obtener los datos de data
        datos = datos['data']

        # Agregar los datos a la lista
        for dato in datos:
            lista.insert(tk.END, dato['name'])
    else:
        lista.insert(tk.END, "Error al obtener datos de la API")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación con Tkinter")
ventana.geometry("1280x720")

# Crear un botón para obtener datos
boton_obtener = tk.Button(ventana, text="Actualizar", command=obtener_datos)
boton_obtener.pack()

# Crear una lista para mostrar los datos
lista = tk.Listbox(ventana)

# Aprovechar la propiedad fill para que la lista ocupe todo el ancho disponible
lista.pack(fill=tk.BOTH, expand=1)

# ejecutar la función obtener_datos() al iniciar la aplicación
obtener_datos()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
