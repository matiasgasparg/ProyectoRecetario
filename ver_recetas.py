import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font,messagebox
import csv
from tkinter import Canvas
from PIL import Image, ImageTk


class VerRecetasWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
    
        self.img_refs = []
        self.nombre=[]
        self.geometry('750x500')
        self.Ingredientes=[]
        self.minsize(200, 200)  # seteamos un tamaño minimo
        self.title("Todas las Recetas")
        self.configure(bg='#056595')            
        self.columns = []

        # Crea botón de eliminar
        self.delete_button = tk.Button(self, text="Eliminar", command=self.delete_selected)
        self.delete_button.grid(row=0, column=1, padx=0, pady=0)
        
        # Crea botón de modificar
        self.modify_button = tk.Button(self, text="Modificar", command=self.modify_selected)
        self.modify_button.grid(row=1, column=1, padx=0, pady=0)
        
        # Creacion del botón buscar
        self.search_button = tk.Button(self, text="Buscar", command=self.search)
        self.search_button.grid(row=2, column=1, padx=0, pady=0)
        
        #Creacion del label para ingresar busaqueda
        self.search_entry=tk.Entry(self)
        self.search_entry.grid(row=3, column=1, padx=0, pady=0)
        #Muestra el nombre de la receta
        self.nombre_value = ttk.Label(self, text='#', foreground='#FFFFFF', font=('Segoe UI', 15), background='#056595')
        self.nombre_value.grid(row=0, column=0, padx=0, pady=0)

        self.ingMostrar_value = ttk.Label(self, text='#', foreground='#FFFFFF', font=('Segoe UI', 15), background='#056595')
        self.ingMostrar_value.grid(row=1, column=0, padx=0, pady=0)


        self.image_label = tk.Label(self)
        self.image_label.grid(row=1, column=2, padx=0, pady=0)
 
        # Crear Treeview
        self.treeview = ttk.Treeview(self, selectmode='browse')
        self.treeview.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=0, pady=0)
        self.treeview.bind("<<TreeviewSelect>>", self.seleccionado)

        # Carga el archivo CSV
        self.load_csv('informacion.csv')



    def load_csv(self, filename):
        # Lee el archivo CSV
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
        # Obtiene los encabezados
            headers = next(reader)
            
        # Configura los encabezados del Treeview
            self.columns = headers
            self.treeview['columns'] = headers
            self.treeview.column("#0", width=0, stretch=False)


            for header in headers:
                self.treeview.heading(header, text=header)
                self.treeview.column(header, anchor='center',minwidth=0, width=font.Font().measure(header)) 
        
        # Agrega datos al Treeview
            for i, row in enumerate(reader):
                self.treeview.insert(parent='', index='end', iid=i, text=str(i), values=row)
                
        # Obtiene la URL de la imagen de la columna Imagen
                img_url = row[1]
        # Cargar la imagen y guardar su referencia
                img = Image.open(img_url)
                img = img.resize((200, 200), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.img_refs.append(img)
        #Obtiene el nombre de la receta
                nomb=row[0]
                self.nombre.append(nomb)
        #Obtiene los datos de ingredientes
                ing = row[7]
                self.Ingredientes.append(ing)



    def seleccionado(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
        # Obtiene el índice de la fila seleccionada
            index = int(self.treeview.item(selected_item)['text'])
        # Obtiene la imagen correspondiente a la fila seleccionada
            img = self.img_refs[index]
            
        # Muestra la imagen en la etiqueta de imagen
            self.image_label.configure(image=img)
            self.image_label.image = img  # Guarda una referencia a la imagen para evitar que sea eliminada por el garbage collector

        # Obtiene los datos de ingredientes correspondientes a la fila seleccionada
            if index < len(self.Ingredientes):
                ing = eval(self.Ingredientes[index])

                print(type(ing))
                print(ing)
                texto_ingredientes = ''

                for i, item in enumerate(ing):
                    texto_ingredientes += f"\n- {item['nombre']}, {item['cantidad']} {item['unidad_medida']}"
                self.ingMostrar_value.configure(text=f'#Ingredientes:{texto_ingredientes}')
            if index<len(self.nombre):
                nomb=self.nombre[index]
                self.nombre_value.configure(text=f'#Nombre: \n-{nomb} ')
   
            


    def delete_selected(self):
        # Checkea si un item esta seleccionado
        if self.treeview.selection():
        # Obtiene item seleccionado
            selected_item = self.treeview.selection()[0]
        # Obtiene el índice del item seleccionado
            index = int(self.treeview.item(selected_item)['text'])
        # Elimina el item del Treeview
            self.treeview.delete(selected_item)
        # Elimina el elemento del archivo CSV
            with open('informacion.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                data = [row for i, row in enumerate(reader) if i != index+1]
            with open('informacion.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)

    def modify_selected(self):
        try:
            # Obtiene item seleccionado
            selected_item = self.treeview.selection()[0]
            # Obtiene índice del item seleccionado
            index = int(self.treeview.item(selected_item)['text'])
            # Obtiene valores de la fila seleccionada
            values = self.treeview.item(selected_item)['values']
            # Crea una ventana de diálogo para modificar los datos
            dialog = tk.Toplevel()
            dialog.title("Modificar datos")
            # Crea campos de entrada para cada columna
            entry_boxes = []
            for i in range(len(self.columns)):
                label = tk.Label(dialog, text=self.columns[i])
                label.grid(row=i, column=0, padx=5, pady=5)
                entry = tk.Entry(dialog, width=30)
                entry.grid(row=i, column=1, padx=5, pady=5)
                entry.insert(0, values[i])
                entry_boxes.append(entry)
            # Crea botones para guardar y cancelar los cambios
            button_frame = tk.Frame(dialog)
            button_frame.grid(row=len(self.columns), column=0, columnspan=2, padx=5, pady=5)
            save_button = tk.Button(button_frame, text="Guardar cambios", command=lambda: self.save_changes(dialog, selected_item, index, entry_boxes))
            save_button.pack(side=tk.LEFT, padx=5, pady=5)
            cancel_button = tk.Button(button_frame, text="Cancelar", command=dialog.destroy)
            cancel_button.pack(side=tk.LEFT, padx=5, pady=5)
        except IndexError:
            # Maensaje de error si no se selecciona una columna
            msj="Seleccione una columna"
            messagebox.showinfo('Aviso', msj)

    def save_changes(self, dialog, selected_item, index, entry_boxes):
    # Obtiene nuevos valores de los campos de entrada
        new_values = [entry.get() for entry in entry_boxes]
    # Actualiza los valores en el Treeview
        self.treeview.item(selected_item, values=new_values)
    # Actualiza los valores en el archivo CSV
        with open('informacion.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for i, row in enumerate(reader) if i != index+1]
        data.append(new_values)
        with open('informacion.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    # Cierra ventana de diálogo
        dialog.destroy()
    def search(self):
        # Obtener el texto ingresado por el usuario
        query = self.search_entry.get().lower()
        # Obtener los índices de las columnas de etiquetas y nombres
        tags_col = self.columns.index('Etiquetas')
        name_col = self.columns.index('Nombre')
        # Eliminar los elementos actuales del Treeview
        self.treeview.delete(*self.treeview.get_children())
        # Leer archivo CSV
        with open('informacion.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            # Ignorar la primera fila (encabezados)
            next(reader)
            # Recorrer las filas del archivo CSV
            for i, row in enumerate(reader):
            # Obtener las etiquetas de la fila actual
                tags = row[tags_col].lower().split(', ')
            # Obtener el nombre de la fila actual
                name = row[name_col].lower()
            # Verificar si la fila actual coincide con la búsqueda
                if query in tags or query in name:
                # Agregar la fila actual al Treeview
                    self.treeview.insert('', 'end', text=str(i), values=row)
        self.search_entry.delete(0,'end')
        
