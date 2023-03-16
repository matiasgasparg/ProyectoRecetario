from tkinter import Toplevel, Entry, Button, Label

class VentanaHija(Toplevel):
    def __init__(self):
        super().__init__()

        # Crear campo de entrada para que el usuario introduzca el nombre
        self.campo_nombre = Entry(self)
        self.campo_nombre.pack()

        # Crear botón para que el usuario confirme el valor introducido
        boton_confirmar = Button(self, text="Confirmar", command=self.confirmar)
        boton_confirmar.pack()

        # Variable para almacenar el valor introducido por el usuario
        self.valor = ""

    def confirmar(self):
        # Recuperar el valor introducido por el usuario y almacenarlo en la variable de la instancia
        self.valor = self.campo_nombre.get()

        # Cerrar la ventana hija
        self.destroy()