import tkinter as tk
from tkinter import filedialog
from tkinter import ttk, messagebox, Toplevel
from Clases.recetario import Recetario
from Clases.ingredientes import Ingredientes
import csv
from PIL import Image, ImageTk
from tkinter import Canvas
from datetime import datetime
import datetime

class ingresar_receta(Toplevel):
    def __init__(self, master):
        Toplevel.__init__(self)     
        self.master = master # referencia a la ventana ppal
        self.geometry('790x800')
        self.config(bg = '#056595')
        self.title('Ingresar Receta')
        self.icono = tk.PhotoImage(file= "IMG/cubiertos.png")
        self.mostrar_ventana = None
        self.treeview = None
        self.resizable(0,0)
        self.etiquetas = []
        self.ingredientes=[]
        self.pasos=[]
        opciones=["kg","g","cm3","cucharadita/s","Tazas"]

        self.Recetario = Recetario()
        self.Ingredientes = Ingredientes()
        
        """FRAMES"""
        self.F_cab = tk.Frame(self)         #Cabecera
        self.F_img=tk.Frame(self)           #Imagen
        self.F_rec = tk.Frame(self)     #Datos de la Receta
        self.F_boton = tk.Frame(self)       #Botones

        """WIDGETS"""
        #Titulo - Principal
        self.Cab_principal = ttk.Label(self.F_cab)

        #Nombre de la receta
        self.nombreReceta_label=ttk.Label(self.F_img)
        self.nombreReceta_input=ttk.Entry(self.F_img)
        #Pasos de la receta
        self.pasosReceta_label=ttk.Label(self.F_img)
        self.pasosReceta_input=ttk.Entry(self.F_img)
        self.pasosReceta_button=ttk.Button(self.F_img)
        #Imagen de la receta
        self.imgRec_label = ttk.Label(self.F_img)
        self.path_text = tk.Text(self.F_img)
        self.canvas = Canvas(self.F_img)
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
        #Favoritos
        self.fav_label=ttk.Label(self.F_rec)
        self.fav_checkbutton=ttk.Checkbutton(self.F_rec)
        #Botones de la receta
        self.upload_button = tk.Button(self.F_img)
        self.ingresarReceta_bott = ttk.Button(self.F_boton)
        self.Cancelar_bott = ttk.Button(self.F_boton)
        #Ingredientes
        self.nombre_input=ttk.Entry(self.F_rec)
        self.nombre_label=ttk.Label(self.F_rec)
        self.cantidad_label=ttk.Label(self.F_rec)
        self.cantidad_input=ttk.Entry(self.F_rec)
        self.option_menu_label=ttk.Label(self.F_rec)
        self.option_menu = ttk.Combobox(self.F_rec, values=opciones)
        #Botones de ingredientes
        self.Mostrar_bott = ttk.Button(self.F_rec)
        self.MostraIng_bott=ttk.Button(self.F_rec)
        self.frames_config()
        self.widgets_config()

        self.frames_grid()
        self.widgets_grid()

        

    def frames_config(self):
        self.F_cab.config(border = 15, bg = '#002B40')
        self.F_img.config(bg = '#056595')
        self.F_rec.config(bg = '#056595')
        self.F_boton.config(bg = '#056595')
    
    def widgets_config(self):
        #Titulo - Principal
        self.Cab_principal.config(text = '------------------Ingresá tu receta!-----------------------', foreground = '#FFFFFF', font = ('Segoe UI Black', 24), background = '#002B40')
        #Nombre de la receta
        self.nombreReceta_label.config(text = 'Nombre de la receta', foreground = '#FFFFFF', font = ('Segoe UI Black', 13), background = '#056595')
        self.nombreReceta_input.config(width=30)
        #Pasos de la receta
        self.pasosReceta_label.config(text = 'Pasos a seguir', foreground = '#FFFFFF', font = ('Segoe UI Black', 13), background = '#056595')
        self.pasosReceta_input.config(width=30)
        self.pasosReceta_button.config(text = 'Agregar', command = self.agregarPasos)
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
        now = datetime.datetime.now()
        self.fechaCrea_input.insert(0,now.strftime("%Y-%m-%d %H:%M:%S"))
        self.fechaCrea_input.config(width = 30)
        #Etiquetas
        self.eti_label.config(text = 'Etiquetas', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.eti_input.config(width = 30)
        self.eti_input.bind('<Return>', self.agregar_etiqueta)
        self.etiquetas_label = ttk.Label(self.F_rec, text='Etiquetas:', foreground='#FFFFFF', font=('Segoe UI Black', 14), background='#056595')
        self.etiquetas_value = ttk.Label(self.F_rec, text='#', foreground='#FFFFFF', font=('Segoe UI', 12), background='#056595')
        #Favorito
        self.fav_label.config(text = 'Favorito?', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.favorito_var = tk.BooleanVar()
        self.fav_checkbutton.config(text="SI",width=10,offvalue=False,variable=self.favorito_var)

        #Ingredientes
        self.nombre_label.config(text = 'Nombre del ingrediente', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.nombre_input.config(width = 30)
        self.cantidad_label.config(text = 'Cantidad del ingrediente', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.cantidad_input.config(width = 30)
    
        self.option_menu_label.config(text = 'Unidad de Medida', foreground = '#FFFFFF', font = ('Segoe UI Black', 10), background = '#002B40')
        self.option_menu.config(width=10)            
        self.Mostrar_bott.config(text = 'Agregar Ingrediente!', command=self.guardar_datos)
        self.MostraIng_bott.config(text='Ver mis ingredientes', command=self.mostrar_datos)
        #Botones

        self.ingresarReceta_bott.config(text = 'Guardar', command = self.Guardar)
        self.Cancelar_bott.config(text = 'Cancelar', command = self.Cancelar)

    def agregar_etiqueta(self, event):
        etiqueta = self.eti_input.get()
        if etiqueta and etiqueta not in self.etiquetas:
            if len(self.etiquetas)<3:
                self.etiquetas.append(etiqueta)
                self.etiquetas_value.config(text=', '.join(self.etiquetas))
                self.eti_input.delete(0, 'end')
            else:            
                messagebox.showinfo("aviso","Solo se aceptan 3 etiquetas")

        else:
            messagebox.showinfo("aviso","La etiqueta ya ha sido ingresada")
    def agregarPasos(self):
        pasos=self.pasosReceta_input.get()


        # Valida que se ingresaron
        if not (pasos):
                messagebox.showerror('Error', 'Debe rellenar Pasos de la receta!')
                
        else:
                self.pasos.append(pasos)

                messagebox.showinfo("aviso","El Paso se ha agregado correctamente,agregue otro!")
        self.pasosReceta_input.delete(0,'end')



    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, columnspan = 100,sticky="ew")
        self.F_img.grid(row=1,column=0)
        self.F_rec.grid(row=2, column=0)
        self.F_boton.grid(row = 3, columnspan = 3)

    def widgets_grid(self):
        #Titulo - Principal
        self.Cab_principal.grid(row = 0)
        #Imagen
        self.imgRec_label.grid(row = 1, column=0, pady = 5)
        #Boton de subir imagen
        self.upload_button.grid(row = 2, column = 0, padx = 10,pady=5)
        #Espacio para la imagen
        self.canvas.grid(row=3,column=0,padx=10)
        #Nombre de la receta
        self.nombreReceta_label.grid(row=4,columnspan=2,pady=5)
        self.nombreReceta_input.grid(row=5,columnspan=2,padx=10)
        #Pasos a seguir
        self.pasosReceta_label.grid(row=6,columnspan=2,pady=5)  
        self.pasosReceta_input.grid(row=7,columnspan=2,padx=10)
        self.pasosReceta_button.grid(row=8,columnspan=2,pady=10)
        #Tiempo de Preparación
        self.tiempoPre_label.grid(row = 8, column = 0, pady = 5)
        self.tiempoPre_input.grid(row = 9, column = 0, padx = 10)
        #Tiempo de Cocción
        self.tiempoCoc_label.grid(row = 8, column = 1, pady = 5)
        self.tiempoCoc_input.grid(row = 9, column = 1, padx = 10)
        #Fecha de creación
        self.fechaCrea_label.grid(row =10, column = 0, pady = 5)
        self.fechaCrea_input.grid(row = 11, column = 0, padx = 10)
        #Etiquetas
        self.eti_label.grid(row=10, column=1, padx=10, pady=5)
        self.eti_input.grid(row=11, column=1, padx=10, pady=5)
    
        # Etiqueta output
        self.etiquetas_label.grid(row=12, column=0, padx=10, sticky='w')
        self.etiquetas_value.grid(row=13, column=0, padx=10, sticky='w')
        #Favorito

        #Botones
        self.ingresarReceta_bott.grid(row = 6, column = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.Cancelar_bott.grid(row = 6, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        #Ingredientes


        self.nombre_label.grid(row =8, column = 4, pady = 5)
        self.nombre_input.grid(row = 9, column = 4,padx = 10)
        self.cantidad_label.grid(row =10, column = 4, pady = 5)
        self.cantidad_input.grid(row = 11, column = 4, padx = 10)
        self.fav_label.grid(row=8,column=5,pady=5)
        self.fav_checkbutton.grid(row=9,column=5,padx=10)
        self.option_menu_label.grid(row = 10, column = 5, pady = 5)
        self.option_menu.grid(row = 11, column = 5, padx = 10)
        self.Mostrar_bott.grid(row = 12,column=4)
        self.MostraIng_bott.grid(row=12,column=5)
    

    def Guardar(self):
        nombre=self.nombreReceta_input.get()
        img = self.path_text.get(1.0, tk.END).strip()
        TiempoPre = self.tiempoPre_input.get()
        tiempoCoc = self.tiempoCoc_input.get()
        fechaCrea = self.fechaCrea_input.get()
        eti = self.etiDevolver()
        fav=self.favorito_var.get()           
        ingredientes=self.ingredientesDevolver()
        pasos=self.pasosDevolver()
        print(f"Estos son los ingredientes {self.ingredientesDevolver()}")
        print(f"Estos son los ingredientes {self.pasosDevolver()}")

        if len(nombre)>0 and len(TiempoPre) > 0 and len(tiempoCoc) > 0 and len(fechaCrea) > 0 and len(eti) > 0 and len(ingredientes) > 0:
            mensaje=self.Recetario.guardar(nombre,img,TiempoPre,tiempoCoc,fechaCrea,eti,fav)
            messagebox.showinfo('Aviso', mensaje)
            fieldnames = ["Nombre","Pasos a seguir","Imagen", "Tiempo de preparacion", "Tiempo de coccion", "Fecha de creacion", "Etiquetas", "Favoritos", "Ingredientes"]

            # Lee las filas existentes del CSV
            recetas = []
            try:
                with open('informacion.csv', mode='r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        recetas.append(row)
            except FileNotFoundError:
                pass
        
            #Busca una receta de igual nombre
            for r in recetas:
                if r['Nombre'] == nombre:
                    r['Pasos a seguir'] = pasos
                    r['Imagen'] = img
                    r['Tiempo de preparacion'] = TiempoPre
                    r['Tiempo de coccion'] = tiempoCoc
                    r['Fecha de creacion'] = fechaCrea
                    r['Etiquetas'] = eti
                    r['Favoritos'] = fav
                    r['Ingredientes'] = ingredientes
                    messagebox.showinfo("aviso","La receta ha sido actualizada")
                    break
            else:
                 # Si no se encuentra crea una nueva
                recetas.append({'Nombre': nombre,'Pasos a seguir':pasos,'Imagen': img, 'Tiempo de preparacion': TiempoPre, 'Tiempo de coccion': tiempoCoc, 'Fecha de creacion': fechaCrea, 'Etiquetas': eti, 'Favoritos': fav, 'Ingredientes': ingredientes})
        
        # Escribe todas las filas

            with open('informacion.csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(recetas)
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')
    def upload_image(self):
        # Abrir cuadro de diálogo para seleccionar archivo de imagen
        filename = filedialog.askopenfilename(initialdir="/", title="Seleccionar imagen", filetypes=(("Archivos de imagen", "*.jpg;*.jpeg;*.png"), ("Todos los archivos", "*.*")))
        
        # Actualizar cuadro de texto con la ubicación del archivo de imagen seleccionado
        self.path_text.delete(1.0, tk.END)
        self.path_text.insert(tk.END, filename)

        # Cargar imagen en el canvas y dimensionarla a 200x200
        try:
            image = Image.open(filename)
            self.image = ImageTk.PhotoImage(image.resize((150, 150), Image.ANTIALIAS))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        except AttributeError:
            mensaje="No seleccionaste ninguna imagen"
            messagebox.showinfo("Aviso",mensaje)
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
                messagebox.showinfo("aviso","El ingrediente se ha agregado correctamente,agregue otro!")
                ingrediente = {'nombre': nombre, 'cantidad': cantidad, 'unidad_medida': unidad_medida}

            # Agregar el ingrediente a la lista
                self.ingredientes.append(ingrediente)
                self.nombre_input.delete(0, 'end')
                self.cantidad_input.delete(0, 'end')
                self.option_menu.delete(0, 'end')
                
            

    def ingredientesDevolver(self):
        a=self.ingredientes
        return a
    def etiDevolver(self):
         b=self.etiquetas
         return b
    def pasosDevolver(self):
         c=self.pasos
         return c
    def report_callback_exception(self, exc, val, tb):
        messagebox.showerror("Error", message=str(val))
    def Cancelar(self):
            self.destroy()
    def mostrar_datos(self):
        # Creamos una nueva ventana para mostrar los datos
        self.mostrar_ventana = tk.Toplevel(self)
        self.mostrar_ventana.geometry('500x300')
        self.mostrar_ventana.title('Mostrar datos')
        self.mostrar_ventana.config(bg='#056595')

        # Creamos un treeview para mostrar los datos en una tabla
        self.treeview = ttk.Treeview(self.mostrar_ventana, columns=('nombre', 'Cantidad', 'unidad_medida'))
        self.treeview.heading('#0', text='Index')
        self.treeview.heading('#1', text='nombre')
        self.treeview.heading('#2', text='cantidad')
        self.treeview.heading('#3', text='unidad_medida')

        # Agregamos los datos a la tabla
        index = 1
        for ingrediente in self.ingredientes:
            self.treeview.insert(parent='', index='end', iid=index, text=index, values=(ingrediente['nombre'], ingrediente['cantidad'], ingrediente['unidad_medida']))
            index += 1

        # Ajustamos las columnas
        self.treeview.column('#0', width=50)
        self.treeview.column('#1', width=200)
        self.treeview.column('#2', width=100)
        self.treeview.column('#3', width=100)

        # Agregamos la tabla a la ventana
        self.treeview.pack(padx=10, pady=10)


 

    def Cancelar(self):
        self.destroy()

