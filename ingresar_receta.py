import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from Clases.recetario import Recetario

class ingresar_receta(Toplevel):
    def __init__(self, master=None,base_datos=None):
        Toplevel.__init__(self, master)
        self.master = master # referencia a la ventana ppal
        self.geometry('418x700')
        self.config(bg = '#056595')
        self.title('Ingresar Receta')
        self.iconbitmap('IMG/cocina2.png')
        self.protocol('WM_DELETE_WINDOW', self.Cancelar)
        self.resizable(0,0)

        self.bdd = base_datos
        self.Recetario = Recetario()
        
        """FRAMES"""
        self.F_cab = tk.Frame(self)         #Cabecera
        self.F_rec = tk.Frame(self)     #Datos de la Receta
        self.F_ing = tk.Frame(self)      #Ingredientes
        self.F_boton = tk.Frame(self)       #Botones

        """WIDGETS"""
        #Titulo - Principal
        self.Cab_principal = ttk.Label(self.F_cab)
        #Titulo - Datos de la Persona
        self.Cab_receta = ttk.Label(self.F_rec)
        #Titulo - Datos de la Cuenta
        self.Cab_ingredientes = ttk.Label(self.F_ing)
        #Imagen de la receta
        self.imgRec_label = ttk.Label(self.F_rec)
        self.imgRec_input = ttk.Entry(self.F_rec)
        #Tiempo de preparación
        self.tiempoPre_label = ttk.Label(self.F_rec)
        self.tiempoPre_input = ttk.Entry(self.F_rec)
        #Tiempo de coccion
        self.tiempoCoc_label = ttk.Label(self.F_rec)
        self.tiempoCoc_input = ttk.Entry(self.F_rec)
        #Fecha de Creación
        self.fechaCrea_label = ttk.Label(self.F_rec)
        self.fechaCrea_input = ttk.Entry(self.F_rec)
        #Etiquetas
        self.eti_label = ttk.Label(self.F_rec)
        self.eti_input = ttk.Entry(self.F_rec)
        #Ingredientes
        self.ing_input=ttk.Label(self.F_ing)
        self.option_menu = tk.OptionMenu(self.F_ing,"Opción 1", "Opción 2", "Opción 3")
        #Botones
        self.ingresarReceta_bott = ttk.Button(self.F_boton)
        self.Cancelar_bott = ttk.Button(self.F_boton)

        self.frames_config()
        self.widgets_config()

        self.frames_grid()
        self.widgets_grid()

        

    def frames_config(self):
        self.F_cab.config(border = 15, bg = '#002B40')
        self.F_rec.config(bg = '#056595')
        self.F_ing.config(bg = '#056595')
        self.F_boton.config(bg = '#056595')
    
    def widgets_config(self):
        #Titulo - Principal
        self.Cab_principal.config(text = 'Ingresá tu receta!', foreground = '#FFFFFF', font = ('Segoe UI Black', 25), background = '#002B40', justify='center')
        #Titulo - Datos la receta
        self.Cab_receta.config(text = 'Ingresa los ingredientes', foreground = '#FFFFFF', font = ('Segoe UI Black', 24), background = '#002B40')
        #Titulo - Ingredientes
        self.Cab_ingredientes.config(text = 'Ingredientes', foreground = '#FFFFFF', font = ('Segoe UI Black', 24), background = '#002B40')
        #Imagen de la receta
        self.imgRec_label.config(text = 'Imagen de la receta', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.imgRec_input.config(width = 30)
        #Tiempo de preparacion
        self.tiempoPre_label.config(text = 'Tiempo de preparación', foreground = '#FFFFFF', font = ('Segoe UI Black', 13), background = '#056595')
        self.tiempoPre_input.config(width = 30)
        #Tiempo de cocción
        self.tiempoCoc_label.config(text = 'Tiempo de Cocción', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.tiempoCoc_input.config(width = 30)
        #Fecha de creación
        self.fechaCrea_label.config(text = 'Fecha de creación', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.fechaCrea_input.config(width = 30)
        #Etiquetas
        self.eti_label.config(text = '#Etiquetas', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.eti_input.config(width = 30)
        #Ingredientes
        self.ing_input.config(width = 30)
        self.option_menu.config(width =5)
        #Botones
        self.ingresarReceta_bott.config(text = 'Guardar', command = self.Guardar)
        self.Cancelar_bott.config(text = 'Cancelar', command = self.Cancelar)

    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, columnspan = 2)
        self.F_rec.grid(row = 1, column = 0, columnspan = 2, pady = 20)
        self.F_ing.grid(row = 2, column = 0, columnspan = 2, pady = 20)
        self.F_boton.grid(row = 3, column = 0, columnspan = 2)

    def widgets_grid(self):
        #Titulo - Principal
        self.Cab_principal.grid(row = 0, ipady = 10)
        #Titulo - Datos de la Receta
        self.Cab_receta.grid(row = 0, column = 0, columnspan = 2)
        #Titulo - Ingredientes
        self.Cab_ingredientes.grid(row = 0, columnspan= 2)
        #Imagen
        self.imgRec_label.grid(row = 1, column = 0, pady = 5)
        self.imgRec_input.grid(row = 2, column = 0, padx = 10)
        #Tiempo de Preparación
        self.tiempoPre_label.grid(row = 1, column = 1, pady = 10)
        self.tiempoPre_input.grid(row = 2, column = 1, padx = 10)
        #Tiempo de Cocción
        self.tiempoCoc_label.grid(row = 3, column = 0, pady = 5)
        self.tiempoCoc_input.grid(row = 4, column = 0, padx = 10)
        #Fecha de creación
        self.fechaCrea_label.grid(row = 3, column = 1, pady = 5)
        self.fechaCrea_input.grid(row = 4, column = 1, padx = 10)
        #Etiquetas
        self.eti_label.grid(row = 5, column = 0, columnspan = 2, pady = 5)
        self.eti_input.grid(row = 6, column = 0, columnspan = 2)
        #Ingredientes
        self.ing_input.grid(row = 2, column = 0, padx = 10)
        self.option_menu.grid(row = 2, column = 1)
       
        #Botones
        self.ingresarReceta_bott.grid(row = 5, column = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.Cancelar_bott.grid(row = 5, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)

    def Guardar(self):
        img = self.imgRec_input.get()
        TiempoPre = self.tiempoPre_input.get()
        tiempoCoc = self.tiempoCoc_input.get()
        fechaCrea = self.fechaCrea_input.get()
        eti = self.eti_input.get()
        ing = self.ing_input.get()

        if len(TiempoPre) > 0 and len(tiempoCoc) > 0 and len(fechaCrea) > 0 and len(eti) > 0 and len(ing) > 0:
            mensaje = self.Recetario.guardar(self.bdd, img, TiempoPre, tiempoCoc, fechaCrea, eti, ing)
            messagebox.showinfo('Aviso', mensaje)
            if mensaje == 'Receta registrada exitosamente!':
                self.Cancelar()
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')

    def Cancelar(self):
        self.destroy()
        self.master.deiconify()

