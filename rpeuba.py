def widgets_config(self):
    # ...
    #Etiquetas
    self.eti_label.config(text='#Etiquetas', foreground='#FFFFFF', font=('Segoe UI Black', 14), background='#056595')
    self.eti_input.config(width=30)

    # Nueva configuración para el input de etiquetas
    self.etiquetas = []
    self.eti_input.bind('<Return>', self.agregar_etiqueta)
    self.etiquetas_label = ttk.Label(self.F_rec, text='Etiquetas:', foreground='#FFFFFF', font=('Segoe UI Black', 14), background='#056595')
    self.etiquetas_value = ttk.Label(self.F_rec, text='', foreground='#FFFFFF', font=('Segoe UI', 12), background='#056595')

    #Botones
    self.ingresarIngrediente_bott.config(text='Ingresar Ingredientes', command=self.ingresar_ingredientes)
    self.ingresarReceta_bott.config(text='Guardar', command=self.Guardar)
    self.Cancelar_bott.config(text='Cancelar', command=self.Cancelar)

def agregar_etiqueta(self, event):
    etiqueta = self.eti_input.get()
    if etiqueta and etiqueta not in self.etiquetas:
        self.etiquetas.append(etiqueta)
        self.etiquetas_value.config(text=', '.join(self.etiquetas))
        self.eti_input.delete(0, 'end')
        Para configurar el input de etiquetas donde el usuario escriba etiquetas y se carguen presionando enter, luego que se muestre abajo de ella las etiquetas que pone el usuario, puedes utilizar el widget Entry y el método bind para detectar cuando se presiona la tecla "Enter" y el widget Label para mostrar las etiquetas ingresadas.

Aquí te muestro cómo puedes modificar el método widgets_config() para agregar estos widgets y configurarlos correctamente:

python
Copy code
def widgets_config(self):
    # ...
    #Etiquetas
    self.eti_label.config(text='#Etiquetas', foreground='#FFFFFF', font=('Segoe UI Black', 14), background='#056595')
    self.eti_input.config(width=30)

    # Nueva configuración para el input de etiquetas
    self.etiquetas = []
    self.eti_input.bind('<Return>', self.agregar_etiqueta)
    self.etiquetas_label = ttk.Label(self.F_rec, text='Etiquetas:', foreground='#FFFFFF', font=('Segoe UI Black', 14), background='#056595')
    self.etiquetas_value = ttk.Label(self.F_rec, text='', foreground='#FFFFFF', font=('Segoe UI', 12), background='#056595')

    #Botones
    self.ingresarIngrediente_bott.config(text='Ingresar Ingredientes', command=self.ingresar_ingredientes)
    self.ingresarReceta_bott.config(text='Guardar', command=self.Guardar)
    self.Cancelar_bott.config(text='Cancelar', command=self.Cancelar)

def agregar_etiqueta(self, event):
    etiqueta = self.eti_input.get()
    if etiqueta and etiqueta not in self.etiquetas:
        self.etiquetas.append(etiqueta)
        self.etiquetas_value.config(text=', '.join(self.etiquetas))
        self.eti_input.delete(0, 'end')

def widgets_grid(self):
    # ...
    #Etiquetas
    self.eti_label.grid(row=5, column=0, padx=10, pady=5, sticky='w')
    self.eti_input.grid(row=5, column=1, padx=10, pady=5, sticky='w')

    # Nuevos widgets
    self.etiquetas_label.grid(row=6, column=0, padx=10, pady=5, sticky='w')
    self.etiquetas_value.grid(row=6, column=1, padx=10, pady=5, sticky='w')

    #Botones
    self.ingresarIngrediente_bott.grid(row=0, column=0, padx=10,