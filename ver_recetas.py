import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font,messagebox
import csv
class VerRecetasWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
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
    

        # Aplica estilo al Treeview
        self.treeview.configure(style="Custom.Treeview")
        # Crea botón de eliminar
        self.delete_button = tk.Button(self, text="Eliminar", command=self.delete_selected)
        self.delete_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Crea botón de modificar
        self.modify_button = tk.Button(self, text="Modificar", command=self.modify_selected)
        self.modify_button.pack(side=tk.BOTTOM, padx=10, pady=10)


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