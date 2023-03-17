import tkinter as tk
from tkinter import ttk
from ingresar_receta import ingresar_receta
class MyGUI(tk.Tk):
    def __init__(self, master):
        tk.Tk.__init__(self)
        self.master = master
        root.title("Recetario")
        root.geometry("500x600")
        
        #root.resizable(False,False)
        fondo = tk.PhotoImage(file="IMG/fondo2.png")#creamos el fondo
        # Crear una imagen de cocina
        lblfondo = tk.Label(root,image=fondo)
        lblfondo.pack()
        #canvas = tk.Canvas(root, width=600, height=200,bg="brown")
        
        #creamos el icolo de la aplicacion
        image_file = tk.PhotoImage(file="IMG/cocina4.png")
        root.iconphoto(True,image_file)
        
        
  
       
        #canvas.create_image(0,-10,anchor = "nw",image=image_file)
        #canvas.pack()
        #canvas.image= image_file # Mantener una referencia a la imagen para evitar que sea eliminada por Python
         #Crear dos botones
        button1 = ttk.Button(self.master, text="Ingresar Receta",command=self.ingresar_receta)
        button2 = ttk.Button(self.master, text="Ver todas las Recetas", command=self.button2_clicked)
        #img_boton = tk.PhotoImage(file="cocina3.png")
        #button3 = tk.Button(text="Buscar archivo", image=img_boton, compound=tk.TOP)
        
        tk.Label
        # Posicionar la imagen y los botones
        #canvas.pack(side=tk.TOP)
        button1.pack(pady=8,ipadx=25,ipady=20)
        button2.pack(pady=8,ipadx=25,ipady=20)
        #button3.place(x=250,y=400)


    def ingresar_receta(self):
        ventana=ingresar_receta(self)
        ventana.mainloop()
        


    def button2_clicked(self):
        print("Botón 2 clickeado")

if __name__ == '__main__':
    root = tk.Tk()
    app = MyGUI(root)
    root.mainloop()