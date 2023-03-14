class Ingredientes():
    def __init__(self,nombre='',unidadDeMedida='',cantidadDeMedida=''):
        self.nombre = nombre
        self.unidadDeMedida = unidadDeMedida
        self.cantidadDeMedida = cantidadDeMedida
    

    def nombre_setter(self, nombre=None):
        self.nombre = nombre.title()
    
    def unidadDeMedida_setter(self,unidadDeMedida):
        self.unidadDeMedida=unidadDeMedida.title()

    def cantidadDeMedida_setter(self,cantidadDeMedida):
        self.cantidadDeMedida=cantidadDeMedida.title()
    def __str__(self):
        return "Nombre de ingrediente: "+ self.nombre + "\nUnidade de medida: "+ self.unidadDeMedida+ "\nCantidad: "+ str(self.cantidad)