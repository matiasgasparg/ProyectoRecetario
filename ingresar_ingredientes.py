
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from Clases.ingredientes import Ingredientes
class Ingresar_ingredientes(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self,master)
        self.geometry('800x800')
        self.config(bg = '#056595')
        self.title('Ingresar Ingrediente')
        self.resizable(0,0)
        opciones=["kg","g","cm3","cucharadita/s","Tazas"]
        self.Ingredientes = Ingredientes()
        self.ingredientes=[]
        #Frames
        self.F_cab = tk.Frame(self)         #Cabecera
        self.F_ing = tk.Frame(self)     #Datos del ingrediente
        self.F_boton = tk.Frame(self)   
        self.F_tree=tk.Frame(self)   
        #Botones
        """WIDGETS"""
        self.Cab_principal = ttk.Label(self.F_cab)
        self.nombre_input=ttk.Entry(self.F_ing)
        self.nombre_label=ttk.Label(self.F_ing)
        self.cantidad_label=ttk.Label(self.F_ing)
        self.cantidad_input=ttk.Entry(self.F_ing)
        self.option_menu_label=ttk.Label(self.F_ing)
        self.option_menu = ttk.Combobox(self.F_ing, values=opciones)
        self.Cancelar_bott = ttk.Button(self.F_boton)
        self.Mostrar_bott = ttk.Button(self.F_boton)

        self.treeview = ttk.Treeview(self.F_tree)

        # Agregar encabezados de columna
        self.treeview['columns'] = ('Nombre', 'Cantidad', 'Unidad de medida')
        self.treeview.heading('#0', text='ID')
        self.treeview.heading('Nombre', text='Nombre')
        self.treeview.heading('Cantidad', text='Cantidad')
        self.treeview.heading('Unidad de medida', text='Unidad de medida')


        self.frames_config()
        self.widgets_config()

        self.frames_grid()
        self.widgets_grid()

    def frames_config(self):
        self.F_cab.config(border = 15, bg = '#002B40')
        self.F_ing.config(bg = '#056595')
        self.F_boton.config(bg = '#056595')
    def widgets_config(self):
        self.Cab_principal.config(text = 'Ingresá tus Ingredientes!', foreground = '#FFFFFF', font = ('Segoe UI Black', 25), background = '#002B40', justify='center')
        self.nombre_label.config(text = '#Nombre', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.nombre_input.config(width = 30)
        self.cantidad_label.config(text = '#Cantidad', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.cantidad_input.config(width = 30)
        self.option_menu_label.config(text = 'Unidad de Medida', foreground = '#FFFFFF', font = ('Segoe UI Black', 10), background = '#002B40')
        self.option_menu.config(width=10)            
        self.Cancelar_bott.config(text = 'Volver', command = self.Cancelar)
        self.Mostrar_bott.config(text = 'Agregar', command = self.guardar_datos)
    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, columnspan = 2)
        self.F_ing.grid(row = 1, column = 0, columnspan = 2, pady = 20)
        self.F_boton.grid(row = 2, column = 0, columnspan = 2)
        self.F_tree.grid(row = 3, column = 0, columnspan = 2)    
    def widgets_grid(self):
        self.Cab_principal.grid(row = 0, ipady = 10)
        self.nombre_label.grid(row = 1, column = 0,columnspan = 2, padx = 10)
        self.nombre_input.grid(row = 2, column = 0,columnspan = 2, padx = 10)


        self.cantidad_label.grid(row = 3, column = 0, padx = 10)
        self.cantidad_input.grid(row = 4, column = 0, padx = 10)

        self.option_menu_label.grid(row = 3, column = 1, padx = 10)
        self.option_menu.grid(row = 4, column = 1, padx = 10)

  
        self.Mostrar_bott.grid(row = 7, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.Cancelar_bott.grid(row = 7, column = 2, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.treeview.grid(row = 10, column = 0, padx = 10)


    def guardar_datos(self):
        nombre = self.nombre_input.get()
        cantidad = self.cantidad_input.get()
        unidad_medida = self.option_menu.get()

        # Validar que se ingresaron todos los datos
        if not (nombre and cantidad and unidad_medida):
            messagebox.showerror('Error', 'Debe ingresar todos los datos')
            return
        # Crear un diccionario con los datos del ingredient
        else:
            ingrediente = {'nombre': nombre, 'cantidad': cantidad, 'unidad_medida': unidad_medida}

            # Agregar el ingrediente a la lista
            self.ingredientes.append(ingrediente)
            # Llamar al método guardar_ingrediente() con la lista de ingredientes
            self.guardar_ingrediente(self.ingredientes)

    def guardar_ingrediente(self, ingredientes):
        # Limpiar la tabla
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Agregar los ingredientes a la tabla
        for i, ingrediente in enumerate(ingredientes):
            self.treeview.insert(parent='', index='end', iid=i, text=i, values=(
                ingrediente['nombre'], ingrediente['cantidad'], ingrediente['unidad_medida']))
    def ingredientesDevolver(self):
        a=self.ingredientes
        return a
    def report_callback_exception(self, exc, val, tb):
        messagebox.showerror("Error", message=str(val))
    def Cancelar(self):
        self.destroy()
 