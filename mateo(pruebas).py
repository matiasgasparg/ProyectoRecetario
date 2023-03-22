import tkinter as a
from tkinter import ttk
vent = a.Tk()
vent.geometry("460x613")
vent.resizable(False,False)
vent.title("Cookbook")
fondo = a.PhotoImage(file="IMG/fondo_titulo_act.png")
icono = a.PhotoImage(file= "IMG/cubiertos.png")
vent.iconphoto(True,icono)
frame = a.Frame(vent)
frame.pack(expand=True,fill="both")

lblfondo = a.Label(frame,image=fondo)
lblfondo.pack(expand=True,fill="both")
frame1 = a.Frame(frame)
boton = ttk.Button(lblfondo,text ="Ingresar recetas",padding=10)
boton2 = ttk.Button(lblfondo,text="Ver todas las recetas",padding=10)
boton_salida = ttk.Button(lblfondo,text="Salir",padding=10)
boton_salida.pack(pady=90,side=a.BOTTOM)
boton2.pack(pady=25,side=a.BOTTOM)
boton.pack(pady=50,side=a.BOTTOM)

vent.mainloop()