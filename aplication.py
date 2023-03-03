import tkinter as tk
from tkinter import ttk
class MyGUI:
    def __init__(self, master):
        self.master = master
        root.title("Recetario")
        root.geometry("500x500")
        background_color = "#272026"
        button_color = "#00b2bc"
        root['background'] = background_color
        
        # Crear una imagen de cocina
        canvas = tk.Canvas(root, width=500, height=200, bg=background_color)
        image_file = tk.PhotoImage(file="cocina4.png")
        canvas.create_image(0, -10, anchor="nw", image=image_file)
        canvas.pack()
        canvas.image= image_file # Mantener una referencia a la imagen para evitar que sea eliminada por Python
     
        # Crear dos botones
        button1 = tk.Button(self.master, text="Ingresar Receta", command=self.button1_clicked)
        button2 = tk.Button(self.master, text="Ver todas las Recetas", command=self.button2_clicked)
        #img_boton = tk.PhotoImage(file="cocina3.png")
        #button3 = tk.Button(text="Buscar archivo", image=img_boton, compound=tk.TOP)

        # Posicionar la imagen y los botones
        canvas.pack(side=tk.TOP)
        button1.place(x=150,y=300)
        button2.place(x=250,y=300)
        #button3.place(x=250,y=400)


    def button1_clicked(self):
        print("Botón 1 clickeado")

    def button2_clicked(self):
        print("Botón 2 clickeado")

if __name__ == '__main__':
    root = tk.Tk()
    app = MyGUI(root)
    root.mainloop()