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

    
    def imgDelPlato_setter(self,imgDelPlato):
        self.imgDelPlato=imgDelPlato

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
    def guardar(self,imgDelPlato,tiemplDePreparacion,tiempoDeCoccion,fechaDeCreacion,etiquetas):
        mensaje=''
        self.imgDelPlato_setter(imgDelPlato)
        self.tiemplDePreparacion_setter(tiemplDePreparacion)
        self.tiempoDeCoccion_setter(tiempoDeCoccion)
        self.fechaDeCreacion_setter(fechaDeCreacion)
        self.etiquetas_setter(etiquetas)

        lista=(self.imgDelPlato,self.tiemplDePreparacion,self.tiempoDeCoccion,self.etiquetas)
        mensaje='Receta registrada exitosamente!'
        return 'Receta registrada exitosamente!'
    def __str__(self):
        return "Numero de receta: " + self.idreceta +"\n lista de Ingredientes: " + self.listaIngredientes + "\nTiempo de preparación: "+ str(self.tiemplDePreparacion) + "\nTiempo de Cocción: " + str(self.tiempoDeCoccion)+ "\Fecha de Creación: " + str(self.fechaDeCreacion)+ "\nEtiquetas: " + str(self.etiquetas)+ "\Es favorito?: " +self.isfavorito
        
