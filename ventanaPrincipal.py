from tkinter import Tk, Button, Label
from ventana_hija import VentanaHija

# Variable global para almacenar el nombre introducido por el usuario
nombre = ""

def abrir_ventana_hija():
    # Crear instancia de la ventana hija
    ventana_hija = VentanaHija()

    # Esperar a que el usuario introduzca los datos y cierre la ventana hija
    ventana_hija.wait_window()

    # Recuperar el valor introducido por el usuario y almacenarlo en la variable global
    global nombre
    nombre = ventana_hija.valor

    # Actualizar la etiqueta en la ventana principal con el valor introducido por el usuario
    etiqueta.config(text="Nombre introducido: " + nombre)

# Crear la ventana principal
ventana_principal = Tk()

# Crear botón para abrir la ventana hija
boton = Button(ventana_principal, text="Abrir ventana hija", command=abrir_ventana_hija)
boton.pack()

# Crear etiqueta para mostrar el valor introducido por el usuario
etiqueta = Label(ventana_principal, text="Nombre introducido: ")
etiqueta.pack()

# Iniciar el bucle principal de eventos
ventana_principal.mainloop()