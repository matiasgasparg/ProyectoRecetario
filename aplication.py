
import tkinter as tk
from tkinter import ttk
#from ingresar_receta import ingresar_receta
import csv
from ver_recetas import VerRecetasWindow
<<<<<<< HEAD
#from PIL import ImageTk, Image
=======
from PIL import ImageTk, Image

>>>>>>> 98294e91ad68fb6f77211194803818e1ea77ee82
class MyGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("460x613")
        self.resizable(False,False)
        self.title("Cookbook")
        self.fondo = tk.PhotoImage(file="IMG/fondo_titulo.png")
        self.icono = tk.PhotoImage(file= "IMG/cubiertos.png")
        self.iconphoto(True,self.icono)
        self.frame = tk.Frame(self)
        self.frame.pack(expand=True,fill="both")

        self.lblfondo = tk.Label(self.frame,image=self.fondo)
        self.lblfondo.pack(expand=True,fill="both")
        self.frame1 = tk.Frame(self.frame)
        self.boton = ttk.Button(self.lblfondo,text="Ingresar recetas",command=self.ingresar_receta,padding=10)
        self.boton2 = ttk.Button(self.lblfondo,text="Ver todas las recetas",command=self.open_ver_recetas,padding=10)
        self.boton_salida = ttk.Button(self.lblfondo,text="Salir",padding=10, command=self.destroy)
        self.boton_salida.pack(pady=60,side=tk.BOTTOM)
        self.boton2.pack(pady=25,side=tk.BOTTOM)
        self.boton.pack(pady=50,side=tk.BOTTOM)

    #def ingresar_receta(self):
        #ventana=ingresar_receta(self)
        #ventana.mainloop()
        
    def open_ver_recetas(self):
        ventana=VerRecetasWindow(self)
        ventana.mainloop()
