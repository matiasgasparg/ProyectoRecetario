import tkinter as tk

# Crea la ventana principal
root = tk.Tk()
root.title("Recetario")
root.geometry("500x500")


# Define los colores de fondo
background_color = "#272026"
button_color = "#00b2bc"
root['background'] = background_color

# Crea un lienzo con una imagen de cocina

canvas = tk.Canvas(root, width=500, height=200, bg=background_color)
image_file = tk.PhotoImage(file="cocina4.png")
canvas.create_image(0, -10, anchor="nw", image=image_file)
canvas.pack()
label.image=image_file
button1 = tk.Button(self.master, text="Botón 1", command=self.button1_clicked)
button2 = tk.Button(self.master, text="Botón 2", command=self.button2_clicked)

        # Posicionar la imagen y los botones
label.pack(side=tk.TOP)
button1.pack(side=tk.LEFT)
button2.pack(side=tk.RIGHT)

def button1_clicked(self):
        print("Botón 1 clickeado")

def button2_clicked(self):
        print("Botón 2 clickeado")
""""
img=tk.PhotoImage(file="cocina4.png")
lbl_image = tk.Label(image=img)
lbl_image.pack()

"""
root.mainloop()