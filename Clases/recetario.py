from Clases.ingredientes import Ingredientes
from datetime import datetime
import csv
class Recetario (Ingredientes):
    def __init__(self,idreceta=None,nombre='',unidadDeMedida='',cantidadDeMedida='',imgDelPlato='',tiemplDePreparacion='',tiempoDeCoccion='',fechaDeCreacion='',etiquetas='',isfavorito=''):
        Ingredientes.__init__(self,nombre,unidadDeMedida,cantidadDeMedida)
        self.imgDelPlato = imgDelPlato
        self.tiemplDePreparacion = tiemplDePreparacion
        self.tiempoDeCoccion = tiempoDeCoccion
        self.fechaDeCreacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.etiquetas= []
        self.isfavorito=False

    def nombre_setter(self, nombre):
        self.nombre=nombre

    def imgDelPlato_setter(self,imgDelPlato):
        self.imgDelPlato=imgDelPlato
    def favorito_setter(self, favorito):
        self.favorito=favorito
    def tiemplDePreparacion_setter(self,tiemplDePreparacion):
        self.tiemplDePreparacion = tiemplDePreparacion
    def tiempoDeCoccion_setter(self,tiempoDeCoccion):
        self.tiempoDeCoccion=tiempoDeCoccion
    def fechaDeCreacion_setter(self,fechaDeCreacion):
        self.fechaDeCreacion=fechaDeCreacion
    def etiquetas_setter(self,etiquetas):
        self.etiquetas=etiquetas
    def isfavorito_setter(self,isfavorito):
        self.isfavorito=isfavorito
    def guardar(self,nombre,imgDelPlato,tiemplDePreparacion,tiempoDeCoccion,fechaDeCreacion,etiquetas,favorito):
        mensaje=''
        self.nombre_setter(nombre)
        self.imgDelPlato_setter(imgDelPlato)
        self.tiemplDePreparacion_setter(tiemplDePreparacion)
        self.tiempoDeCoccion_setter(tiempoDeCoccion)
        self.fechaDeCreacion_setter(fechaDeCreacion)
        self.etiquetas_setter(etiquetas)
        self.favorito_setter(favorito)

        lista=(self.nombre,self.imgDelPlato,self.tiemplDePreparacion,self.tiempoDeCoccion,self.etiquetas,self.favorito)
        mensaje='Receta registrada exitosamente!'
        return 'Receta registrada exitosamente!'
        
