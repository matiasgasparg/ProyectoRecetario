import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from Clases.ingredientes import Ingredientes

class Ingresar_ingredientes(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master)
        self.master = master # referencia a la ventana ppal
        self.geometry('418x600')
        self.config(bg = '#056595')
        self.title('Ingresar Ingrediente')
        self.protocol('WM_DELETE_WINDOW', self.Cancelar)
        self.resizable(0,0)
        opciones=["kg","g","cm3","cucharadita/s","Tazas"]
        self.Ingredientes = Ingredientes()

        #Frames
        self.F_cab = tk.Frame(self)         #Cabecera
        self.F_ing = tk.Frame(self)     #Datos del ingrediente
        self.F_boton = tk.Frame(self)       #Botones
        """WIDGETS"""
        self.Cab_principal = ttk.Label(self.F_cab)
        self.nombre_input=ttk.Entry(self.F_ing)
        self.nombre_label=ttk.Label(self.F_ing)
        self.cantidad_label=ttk.Label(self.F_ing)
        self.cantidad_input=ttk.Entry(self.F_ing)
        self.option_menu_label=ttk.Label(self.F_ing)
        self.option_menu = ttk.Combobox(self.F_ing, values=opciones)
        self.ingresarReceta_bott = ttk.Button(self.F_boton)
        self.Cancelar_bott = ttk.Button(self.F_boton)
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
        self.ingresarReceta_bott.config(text = 'Guardar', command = self.guardar_ingrediente)
        self.Cancelar_bott.config(text = 'Cancelar', command = self.Cancelar)
    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, columnspan = 2)
        self.F_ing.grid(row = 1, column = 0, columnspan = 2, pady = 20)
        self.F_boton.grid(row = 2, column = 0, columnspan = 2)     
    def widgets_grid(self):
        self.Cab_principal.grid(row = 0, ipady = 10)
        self.nombre_label.grid(row = 1, column = 0,columnspan = 2, padx = 10)
        self.nombre_input.grid(row = 2, column = 0,columnspan = 2, padx = 10)


        self.cantidad_label.grid(row = 3, column = 0, padx = 10)
        self.cantidad_input.grid(row = 4, column = 0, padx = 10)

        self.option_menu_label.grid(row = 3, column = 1, padx = 10)
        self.option_menu.grid(row = 4, column = 1, padx = 10)

  

        self.ingresarReceta_bott.grid(row = 7, column = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.Cancelar_bott.grid(row = 7, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)
 
    def guardar_ingrediente(self):
        nombre=self.nombre_input.get()
        cantidad=self.cantidad_input.get()
        option=self.option_menu.get()
        if len(nombre) > 0 and len(cantidad) > 0 and len(option) > 0:
            mensaje = self.Ingredientes.guardar_ingredientes(nombre, cantidad, option)
            messagebox.showinfo('Aviso', mensaje)
            if mensaje == 'Ingrediente registrado exitosamente!':
                self.mainloop()
                self.master.deiconify()
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')


    def ingredientesDevolver(self):
        return self.Ingredientes.devolver()
    def report_callback_exception(self, exc, val, tb):
        messagebox.showerror("Error", message=str(val))
    def Cancelar(self):
        try:
            self.destroy()
            self.ingresar_receta.deiconify()
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrió un error al cerrar la ventana: {str(e)}')
