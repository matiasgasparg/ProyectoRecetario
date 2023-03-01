class Ingrediente():
    def __init__(self,nombre,unidadDeMedida,cantidadDeMedida):
        self.nombre = nombre
        self.unidadDeMedida = unidadDeMedida
        self.cantidadDeMedida = cantidadDeMedida
    
    @property
    def nombre(self):
        return self.nombre
    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre
    @property
    def unidadDeMedida(self):
        return self.unidadDeMedida
    @unidadDeMedida.setter
    def unidadDeMedida(self, unidadDeMedida):
        self.unidadDeMedida = unidadDeMedida
    @property
    def cantidadDeMedida(self):
        return self.cantidadDeMedida
    @cantidadDeMedida.setter
    def cantidadDeMedida(self, cantidadDeMedida):
        self.cantidadDeMedida =cantidadDeMedida
    def __str__(self):
        return "Nombre de ingrediente: "+ self.nombre + "\nUnidade de medida: "+ self.unidadDeMedida+ "\nCantidad: "+ str(self.cantidad)