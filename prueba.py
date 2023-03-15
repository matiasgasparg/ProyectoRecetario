import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from Clases.ingredientes import Ingredientes

class ingresar_ingredientes(Toplevel):
    def __init__(self, master=None,base_datos=None):
        Toplevel.__init__(self, master)
        self.geometry('600x500')
        self.config(bg = '#056595')
        self.title('Ingredientes')

        #Botón para agregar nuevos widgets
        self.agregar_bott = ttk.Button(self, text='Agregar', command=self.agregar_widgets)
        self.agregar_bott.pack(pady=10)

    def agregar_widgets(self):
        #Crear nuevos widgets
        nuevo_label=ttk.Label(self,text="Ingrediente")
        nuevo_input = ttk.Entry(self)
        nuevo_label2=ttk.Label(self,text="Unidad de medida")
        opciones = ['Opción 1', 'Opción 2', 'Opción 3']
        nuevo_menu = ttk.Combobox(self, values=opciones)
        nuevo_label3=ttk.Label(self,text="Cantidad")
        nuevo_input2= ttk.Entry(self)

        #Configurar los widgets
        nuevo_input.config(width=30)
        nuevo_menu.config(width=10)

        #Agregar los widgets a la ventana
        nuevo_label.pack(pady=5)
        nuevo_input.pack(pady=5)
        nuevo_label2.pack(pady=5)
        nuevo_menu.pack (pady=5)
        nuevo_label3.pack(pady=5)
        nuevo_input2.pack(pady=5)

