from tkinter import messagebox
from aplication import MyGUI


try:

    a = MyGUI()
    a.mainloop()

except:
    
    messagebox.showerror('Error en la aplicación', 'Algo salio mal')