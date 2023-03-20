import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font,messagebox
import csv
import urllib.request
from PIL import Image, ImageTk

class VerRecetasWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.img_refs = []
        self.geometry('780x800')
        self.image_label = tk.Label(self)
        self.image_label.pack(side=tk.BOTTOM, pady=10)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0) 
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.minsize(400, 200)  # seteamos un tamaño minimo

        self.title("Todas las Recetas")
        self.configure(bg='#056595')            
        self.columns = []
         # Configura estilo para el Treeview

        style = ttk.Style()
        style.configure("Custom.Treeview", background="#056595")
        # Crear Treeview
        self.treeview = ttk.Treeview(self,style="Custom.Treeview", selectmode='browse')
        self.treeview.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    

        # Crear Scrollbar horizontal
        self.treeview_scrollbar_x = ttk.Scrollbar(self.treeview, orient='horizontal', command=self.treeview.xview)
        self.treeview_scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Vincular Scrollbar horizontal al Treeview
        self.treeview.configure(xscrollcommand=self.treeview_scrollbar_x.set)
        # Aplica estilo al Treeview
        self.treeview.configure(style="Custom.Treeview")
        # Crea botón de eliminar
        self.delete_button = tk.Button(self, text="Eliminar", command=self.delete_selected)
        self.delete_button.pack(side=tk.BOTTOM, padx=10, pady=10)
        #Creacion del botón buscar
        self.search_button = tk.Button(self, text="Buscar", command=self.search)
        self.search_entry=tk.Entry(self,text="Buscar por nombre")
        self.search_entry.pack(side=tk.BOTTOM,padx=10,pady=10)

        self.search_button.pack(side=tk.TOP, padx=10, pady=10)
        # Crea botón de modificar
        self.modify_button = tk.Button(self, text="Modificar", command=self.modify_selected)
        self.modify_button.pack(side=tk.BOTTOM, padx=10, pady=10)
        self.treeview.bind("<<TreeviewSelect>>", self.on_select)


        # Carga archivo CSV
        self.load_csv('informacion.csv')



    def load_csv(self, filename):
        # Leer archivo CSV
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
        # Obtiene encabezados
            headers = next(reader)
        # Configura encabezados del Treeview
            self.columns = headers
            self.treeview['columns'] = headers
            self.treeview.heading('#0', text='Índice')


            for header in headers:
                self.treeview.heading(header, text=header)
                self.treeview.column(header, anchor='center',minwidth=0, width=font.Font().measure(header))  # Agregar esta línea
        
        # Agrega datos al Treeview
            for i, row in enumerate(reader):
                self.treeview.insert(parent='', index='end', iid=i, text=str(i), values=row)
                
        # Obtener la URL de la imagen de la columna Imagen
                img_url = row[1]
        # Cargar imagen y guardar su referencia
                img = Image.open(img_url)
                img = img.resize((200, 200), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.img_refs.append(img)
    def on_select(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
        # Obtener el índice de la fila seleccionada
            index = int(self.treeview.item(selected_item)['text'])
        # Obtener la imagen correspondiente a la fila seleccionada
            img = self.img_refs[index]
        # Mostrar la imagen en la etiqueta de imagen
            self.image_label.configure(image=img)
            self.image_label.image = img  # Guarda una referencia a la imagen para evitar que sea eliminada por el garbage collector         
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
        # Actualiza valores en el Treeview
        self.treeview.item(selected_item, values=new_values)
        # Actualiza valores en el archivo CSV
        with open('informacion.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for i, row in enumerate(reader) if i != index+1]
        with open('informacion.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.columns)
            for i, row in enumerate(data):
                if i == index:
                    writer.writerow(new_values)
                else:
                    writer.writerow(row)
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
        
