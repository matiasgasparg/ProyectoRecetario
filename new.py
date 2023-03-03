import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(10))
        self.parent = parent # referencia a la ventana ppal
        parent.title("Receta")
        self.listaDeIngredientes=tk.StringVar()
        self.imgDelPlato = tk.StringVar()
        self.tiemplDePreparacion = tk.StringVar()
        self.tiempoDeCoccion = tk.StringVar()
        self.fechaDeCreacion=tk.StringVar()
        self.etiquetas=tk.StringVar()
        self.isfavorito=tk.StringVar()
        ttk.Label(self, text="Lista de ingredientes", padding=3).grid(row=0, column=1)
        ttk.Entry(self, textvariable=self.listaDeIngredientes).grid(row=0, column=2)
        ttk.Label(self, text="Imagen del Plato", padding=3).grid(row=1, column=1)
        ttk.Entry(self, textvariable=self.imgDelPlato).grid(row=1, column=2)
        ttk.Label(self, text="Tiempo de Preparación", padding=3).grid(row=2, column=1)
        ttk.Entry(self, textvariable=self.tiemplDePreparacion).grid(row=2, column=2)
        ttk.Label(self, text="Tiempo de Cocción", padding=3).grid(row=3, column=1)
        ttk.Entry(self,textvariable=self.tiempoDeCoccion).grid(row=3, column=2)
        ttk.Label(self, text="Etiquetas", padding=3).grid(row=4, column=1)
        ttk.Entry(self,textvariable=self.etiquetas).grid(row=4, column=2)        
        btn_guardar = ttk.Button(self, text="Guardar", padding=3, command=self.guardar)
        btn_guardar.grid(row=10, column=3)
        parent.bind('<Return>', lambda e: btn_guardar.invoke()) # para ejecutar el btn al presionar enter
    def guardar(self):
        print(f"Guardados los datos: {self.listaDeIngredientes.get()}, {self.imgDelPlato.get()}, {self.tiemplDePreparacion.get()},{self.tiemplDePreparacion.get},{self.tiempoDeCoccion.get},{self.etiquetas.get} ")
        self.parent.destroy() # terminamos el programa al destruir la ventana ppal

root = tk.Tk()
App(root).grid()
root.resizable(False, False) # evita que se pueda cambiar de tamaño la ventana
root.mainloop()