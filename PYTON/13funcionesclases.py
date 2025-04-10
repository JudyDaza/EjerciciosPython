#clases  
class  Gato:
    def __init__(self,nombre,color,raza,edad,peso):
        self.nombre = nombre 
        self.color = color
        self.raza = raza 
        self.edad = edad
        self.peso = peso  
        print(f"Se ha creado la clase gato {self.nombre} de color {self.color} y raza {self.raza} es un bebe   {self.edad}")
        input ("precione enter para continuar")

    def decribir (self):
        print(f" {self.nombre} it is a colored cat {self.color} ")
        input(f"{self.nombre} press enter to continue")

    def maullar (self):
        print(f" {self.nombre} dice miau ")
        input(f"{self.nombre} pulse enter para continuar")

    def peso (sefl):
        print(f"{sefl.nombre} come demasiado poe eso es gordo ")
        input(f"{sefl.nombre} pulse enter para continuar")

mi_gato=Gato("Daemon", "blanco", "siames" , "1 año", "8 kg")
mi_gato.decribir()
mi_gato.maullar()
