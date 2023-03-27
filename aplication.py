
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from ingresar_receta import ingresar_receta
import csv
from ver_recetas import VerRecetasWindow
from PIL import ImageTk, Image
import random
import os


class MyGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("460x613")
        self.resizable(False,False)
        self.title("Cookbook")
        self.fondo = tk.PhotoImage(file="IMG/fondo_titulo_act.png")
        self.icono = tk.PhotoImage(file= "IMG/cubiertos.png")
        self.iconphoto(True,self.icono)
        self.frame = tk.Frame(self)
        self.frame.pack(expand=True,fill="both")
        self.lblfondo = tk.Label(self.frame,image=self.fondo)
        self.lblfondo.pack(expand=True,fill="both")
        self.boton = ttk.Button(self.lblfondo,text="Ingresar recetas",command=self.ingresar_receta,padding=10)
        self.boton2 = ttk.Button(self.lblfondo,text="Ver todas las recetas",command=self.ver_receta,padding=10)
        self.boton_mostarReceta = ttk.Button(self.lblfondo,text="Receta del dia ",padding=10, command=self.mostrar_receta)
        self.boton_mostarReceta.pack(pady=60,side=tk.BOTTOM)
        self.boton2.pack(pady=25,side=tk.BOTTOM)
        self.boton.pack(pady=50,side=tk.BOTTOM)
        #Crea el treeview
        self.treeview = ttk.Treeview(self.frame)
        
        self.treeview.config(height=1)
        self.treeview.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)
        #Crea la barra horizontal 
        self.treeview_scrollbar_x = ttk.Scrollbar(self.treeview, orient='horizontal', command=self.treeview.xview)
        self.treeview_scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
    def mostrar_receta(self):
        try:
            with open('informacion.csv') as csvfile:
                reader = csv.reader(csvfile,skipinitialspace=True)
                next(reader)
                data = list(reader)
                random_row = random.choice(data)
                self.treeview.delete(*self.treeview.get_children())
                self.treeview["columns"] = ["1","2","3","4","5"]
                self.treeview.column("#0", width=0, stretch=False)
                self.treeview.heading("1", text="Nombre")
                self.treeview.column("1", width=50, stretch=False,anchor='center')
                self.treeview.heading("2", text="Tiempo de preparacion",anchor='center')
                self.treeview.column("2", width=50, stretch=False,anchor='center')
                self.treeview.heading("3", text="Tiempo de coccion",anchor='center')
                self.treeview.column("3", width=50, stretch=False,anchor='center')
                self.treeview.heading("4", text="Pasos a seguir",anchor='center')
                self.treeview.column("4", width=50, stretch=True,anchor='center')
                self.treeview.heading("5", text="Ingredientes",anchor='center')
                self.treeview.column("5", width=50, stretch=True,anchor='center')
                self.treeview.insert("", "end", values=(random_row[0], random_row[3], random_row[4],random_row[1],random_row[8]))
                self.treeview.pack(expand=True, fill='both')
        except FileNotFoundError:
                
                 messagebox.showerror('Error', 'No hay recetas,Ingresa una receta!')

            

    def ingresar_receta(self):
 
        ventana=ingresar_receta(self)
        ventana.mainloop()
        
    def ver_receta(self):
        nombre_archivo = "informacion.csv"

        if os.path.isfile(nombre_archivo):
            ventana=VerRecetasWindow(self)
            ventana.mainloop()

        else:
            messagebox.showerror('Error', 'No hay recetas,Ingresa una receta!')
   
