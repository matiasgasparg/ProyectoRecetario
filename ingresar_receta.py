import tkinter as tk
from tkinter import Tk, Button, Label
from tkinter import filedialog
from tkinter import ttk, messagebox, Toplevel
from Clases.recetario import Recetario
from ingresar_ingredientes import Ingresar_ingredientes
from Clases.ingredientes import Ingredientes
import csv
from PIL import Image, ImageTk
from tkinter import Canvas

class ingresar_receta(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self)
        self.master = master # referencia a la ventana ppal
        self.geometry('430x700')
        self.config(bg = '#056595')
        self.title('Ingresar Receta')
        self.iconbitmap('IMG/cocina2.png')
        self.resizable(0,0)
        self.Ingresar_ingredientes=Ingresar_ingredientes()

        self.Recetario = Recetario()
        self.Ingredientes = Ingredientes()
        
        """FRAMES"""
        self.F_cab = tk.Frame(self)         #Cabecera
        self.F_rec = tk.Frame(self)     #Datos de la Receta
        self.F_ing = tk.Frame(self)      #Ingredientes
        self.F_boton = tk.Frame(self)       #Botones

        """WIDGETS"""
        #Titulo - Principal
        self.Cab_principal = ttk.Label(self.F_cab)
        #Titulo - Datos de los ingredientes
        self.Cab_ingredientes = ttk.Label(self.F_ing)
        #Imagen de la receta
        self.imgRec_label = ttk.Label(self.F_rec)
        self.path_text = tk.Text(self.F_rec)
        self.canvas = Canvas(self.F_rec)
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

        #Botones
        self.upload_button = tk.Button(self.F_rec)
        self.ingresarIngrediente_bott=ttk.Button(self.F_boton)
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
        #Titulo - Ingredientes
        self.Cab_ingredientes.config(text = 'Ingredientes', foreground = '#FFFFFF', font = ('Segoe UI Black', 24), background = '#002B40')
        #Imagen de la receta
        self.imgRec_label.config(text = 'Imagen de la receta', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.canvas.config(width=150, height=150)
        self.upload_button.config(text="Subir imagen", command=self.upload_image)
        self.image = None # Variable para almacenar la imagen cargada
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
        #Botones
        self.ingresarIngrediente_bott.config(text = 'Ingresar Ingredientes', command = self.ingresar_ingredientes)
        self.ingresarReceta_bott.config(text = 'Guardar', command = self.Guardar)
        self.Cancelar_bott.config(text = 'Cancelar', command = self.Cancelar)

    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, columnspan = 2)
        self.F_rec.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        self.F_ing.grid(row = 2, column = 0, columnspan = 2, pady = 20)
        self.F_boton.grid(row = 3, column = 0, columnspan = 2)

    def widgets_grid(self):
        #Titulo - Principal
        self.Cab_principal.grid(row = 0)
        #Titulo - Ingredientes
        self.Cab_ingredientes.grid(row = 0, columnspan= 2)
        #Imagen
        self.imgRec_label.grid(row = 1, columnspan= 2, pady = 5)
        #Boton de subir imagen
        self.upload_button.grid(row = 2, columnspan = 2, padx = 10,pady=5)
        #Espacio para la imagen
        self.canvas.grid(row=3,columnspan=2,padx=10)

        #Tiempo de Preparación
        self.tiempoPre_label.grid(row = 4, column = 0, pady = 5)
        self.tiempoPre_input.grid(row = 5, column = 0, padx = 10)
        #Tiempo de Cocción
        self.tiempoCoc_label.grid(row = 4, column = 1, pady = 5)
        self.tiempoCoc_input.grid(row = 5, column = 1, padx = 10)
        #Fecha de creación
        self.fechaCrea_label.grid(row = 6, column = 0, pady = 5)
        self.fechaCrea_input.grid(row = 7, column = 0, padx = 10)
        #Etiquetas
        self.eti_label.grid(row = 6, column = 1, columnspan = 2, pady = 5)
        self.eti_input.grid(row = 7, column = 1, columnspan = 2)

       
        #Botones
        self.ingresarIngrediente_bott.grid(row = 2, column = 0, columnspan = 2,pady = 5)
        self.ingresarReceta_bott.grid(row = 5, column = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.Cancelar_bott.grid(row = 5, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)
    
    def ingresar_ingredientes(self):
        self.withdraw
        ventana=Ingresar_ingredientes(self)
        ventana.mainloop()

    def Guardar(self):
        img = self.path_text.get(1.0, tk.END).strip()
        TiempoPre = self.tiempoPre_input.get()
        tiempoCoc = self.tiempoCoc_input.get()
        fechaCrea = self.fechaCrea_input.get()
        eti = self.eti_input.get()
        
        ingredientes=self.Ingresar_ingredientes.ingredientesDevolver()
        print(f"Estos son los ingredientes {self.Ingresar_ingredientes.ingredientesDevolver()}")
        recetas=[img,TiempoPre,tiempoCoc,fechaCrea,eti,ingredientes]
        if len(TiempoPre) > 0 and len(tiempoCoc) > 0 and len(fechaCrea) > 0 and len(eti) > 0 and len(ingredientes) > 0:
            mensaje=self.Recetario.guardar(img,TiempoPre,tiempoCoc,fechaCrea,eti)
            messagebox.showinfo('Aviso', mensaje)
            if mensaje == 'Receta registrada exitosamente!':
                    self.Cancelar()
                    
            try:
                with open('informacion.csv', mode='r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        recetas.append(row)
            except FileNotFoundError:
                pass
            with open('informacion.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([img, TiempoPre,tiempoCoc,fechaCrea,eti,ingredientes])
        else:
     
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')
    def upload_image(self):
        # Abrir cuadro de diálogo para seleccionar archivo de imagen
        filename = filedialog.askopenfilename(initialdir="/", title="Seleccionar imagen", filetypes=(("Archivos de imagen", "*.jpg;*.jpeg;*.png"), ("Todos los archivos", "*.*")))
        
        # Actualizar cuadro de texto con la ubicación del archivo de imagen seleccionado
        self.path_text.delete(1.0, tk.END)
        self.path_text.insert(tk.END, filename)

        # Cargar imagen en el canvas y dimensionarla a 200x200
        image = Image.open(filename)
        self.image = ImageTk.PhotoImage(image.resize((200, 200), Image.ANTIALIAS))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
  
    def Cancelar(self):
        self.destroy()
        self.master.iconify()

