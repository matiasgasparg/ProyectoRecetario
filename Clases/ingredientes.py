class Ingredientes():
    def __init__(self,nombre='',unidadDeMedida='',cantidadDeMedida=''):
        self.nombre = nombre
        self.unidadDeMedida = unidadDeMedida
        self.cantidadDeMedida = cantidadDeMedida
    

    def nombre_setter(self, nombre):
        self.nombre = nombre
    
    def unidadDeMedida_setter(self,unidadDeMedida):
        self.unidadDeMedida=unidadDeMedida
    def cantidadDeMedida_setter(self,cantidadDeMedida):
        self.cantidadDeMedida=cantidadDeMedida

    def guardar_ingredientes(self,nombre,unidadDeMedidad,cantidadDeMedida):
        self.nombre_setter(nombre)
        self.unidadDeMedida_setter(unidadDeMedidad)
        self.cantidadDeMedida_setter(cantidadDeMedida)
        return 'Ingrediente registrado exitosamente!'
    def devolver(self):
        nombre=self.nombre
        unidad=self.unidadDeMedida
        cantidad=self.cantidadDeMedida
        lista=[nombre,unidad,cantidad]
        return lista
    def __str__(self):
        return "Nombre de ingrediente: "+ self.nombre + "\nUnidade de medida: "+ self.unidadDeMedida+ "\nCantidad: "+ str(self.cantidadDeMedida)


prueba=Ingredientes()
prueba.guardar_ingredientes("Arroz","KG","100")
prueba.devolver()
