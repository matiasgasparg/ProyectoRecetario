import tkinter as a
from tkinter import ttk
vent = a.Tk()
vent.geometry("450x500")
vent.resizable(False,False)
fondo = a.PhotoImage(file="IMG/fondo2.png")
titulo = a.PhotoImage(file = "IMG/cocina4.png")
frame = a.Frame(vent)
frame.pack(expand=True,fill="both")

lblfondo = a.Label(frame,image=fondo)
lblfondo.pack(expand=True,fill="both")
frame1 = a.Frame(frame)
boton = a.Button(lblfondo,text="boton largo")
boton.pack(padx=200,pady=200,side=a.BOTTOM,)


vent.mainloop()