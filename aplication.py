import tkinter as tk
from tkinter import ttk
from ingresar_receta import ingresar_receta
import csv
from ver_recetas import VerRecetasWindow
from PIL import ImageTk, Image
class MyGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Recetario")
        self.geometry("500x500")
        background_color = "#272026"
        button_color = "#00b2bc"
        self['background'] = background_color
        # Crear una imagen de cocina
        canvas = tk.Canvas(self, width=500, height=200, bg=background_color)
        image_file = tk.PhotoImage(file="IMG/cocina4.png")
        canvas.create_image(0, -10, anchor="nw", image=image_file)
        canvas.pack()
        canvas.image= image_file # Mantener una referencia a la imagen para evitar que sea eliminada por Python
     
        # Crear dos botones
        button1 = tk.Button(self.master, text="Ingresar Receta", command=self.ingresar_receta)
        button2 = tk.Button(self.master, text="Ver todas las Recetas", command=self.open_ver_recetas)
        #img_boton = tk.PhotoImage(file="cocina3.png")
        #button3 = tk.Button(text="Buscar archivo", image=img_boton, compound=tk.TOP)

        # Posicionar la imagen y los botones
        canvas.pack(side=tk.TOP)
        button1.place(x=150,y=300)
        button2.place(x=250,y=300)
        #button3.place(x=250,y=400)


    def ingresar_receta(self):
        self.withdraw
        ventana=ingresar_receta(self)
        ventana.mainloop()
        
    def open_ver_recetas(self):
        self.withdraw
        ventana=VerRecetasWindow(self)
        ventana.mainloop()