class Recetario ():
    def __init__(self,idreceta,listaIngredientes,imgDelPlato,tiemplDePreparacion,tiempoDeCoccion,fechaDeCreacion,etiquetas,isfavorito):
        self.idreceta = idreceta
        self.listaIngredientes=listaIngredientes
        self.imgDelPlato = imgDelPlato
        self.tiemplDePreparacion = tiemplDePreparacion
        self.tiempoDeCoccion = tiempoDeCoccion
        self.fechaDeCreacion = fechaDeCreacion
        self.etiquetas= etiquetas
        self.isfavorito=isfavorito

    @property
    def idreceta(self):
        return self.idreceta
    
    @property
    def listaIngredientes(self):
        return self._listaIngredientes
    @listaIngredientes.setter
    def listaIngredientes(self,listaIngredientes):
        self._listaIngredientes = listaIngredientes
    @property
    def imgDelPlato(self):
        return self.imgDelPlato
    @imgDelPlato.setter
    def imgDelPlato(self,imgDelPlato):
        self.imgDelPlato = imgDelPlato
    @property
    def tiemplDePreparacion(self):
        return self.tiemplDePreparacion
    @tiemplDePreparacion.setter
    def tiemplDePreparacion(self,tiemplDePreparacion):
        self.tiemplDePreparacion=tiemplDePreparacion
    @property
    def tiempoDeCoccion(self):
        return self.tiempoDeCoccion
    @tiempoDeCoccion.setter
    def tiempoDeCoccion(self,tiempoDeCoccion):
        self.tiempoDeCoccion = tiempoDeCoccion
    @property
    def fechaDeCreacion(self):
        return self.fechaDeCreacion
    @fechaDeCreacion.setter
    def fechaDeCreacion(self,fechaDeCreacion):
        self.fechaDeCreacion = fechaDeCreacion
    @property
    def etiquetas(self):
        return self.etiquetas
    @etiquetas.setter
    def etiquetas(self,etiquetas):
        self.etiquetas = etiquetas
    @property
    def isfavorito(self):
        return self.isfavorito
    @isfavorito.setter
    def isfavorito(self,isfavorito):
        self.isfavorito = isfavorito 
    def __str__(self):
        return "Numero de receta: " + self.idreceta +"\n lista de Ingredientes: " + self.listaIngredientes + "\nTiempo de preparación: "+ str(self.tiemplDePreparacion) + "\nTiempo de Cocción: " + str(self.tiempoDeCoccion)+ "\Fecha de Creación: " + str(self.fechaDeCreacion)+ "\nEtiquetas: " + str(self.etiquetas)+ "\Es favorito?: " +self.isfavorito
        
