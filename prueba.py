import tkinter as tk
import csv

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Ventana Principal")

        # Crear botón para abrir ventana hija
        self.btn_abrir = tk.Button(master, text="Abrir ventana hija", command=self.abrir_ventana_hija)
        self.btn_abrir.pack()

    def abrir_ventana_hija(self):
        # Crear ventana hija
        ventana_hija = tk.Toplevel(self.master)
        ventana_hija.title("Ventana Hija")

        # Crear etiquetas y campos de entrada para obtener información
        self.lbl_nombre = tk.Label(ventana_hija, text="Nombre:")
        self.lbl_nombre.grid(row=0, column=0)
        self.txt_nombre = tk.Entry(ventana_hija)
        self.txt_nombre.grid(row=0, column=1)

        self.lbl_edad = tk.Label(ventana_hija, text="Edad:")
        self.lbl_edad.grid(row=1, column=0)
        self.txt_edad = tk.Entry(ventana_hija)
        self.txt_edad.grid(row=1, column=1)

        # Crear botón para guardar información en archivo csv
        self.btn_guardar = tk.Button(ventana_hija, text="Guardar", command=self.guardar_info_csv)
        self.btn_guardar.grid(row=2, column=0, columnspan=2)

    def guardar_info_csv(self):
        # Obtener información ingresada en la ventana hija
        nombre = self.txt_nombre.get()
        edad = self.txt_edad.get()

        # Guardar información en archivo csv
        with open('informacion.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nombre, edad])

        # Cerrar ventana hija después de guardar información
        self.master.focus_set()

# Crear ventana principal
root = tk.Tk()
ventana_principal = VentanaPrincipal(root)
root.mainloop()