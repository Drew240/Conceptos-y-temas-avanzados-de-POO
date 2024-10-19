class Vehiculo:
    def arrancar(self):
        pass

    def parar(self):
        pass

class Carro(Vehiculo):
    def arrancar(self):
        return "El carro está arrancando."

    def parar(self):
        return "El carro se ha detenido."

# Crear un objeto de la clase Carro
mi_carro = Carro()

# Utilizar los métodos
print(mi_carro.arrancar())
print(mi_carro.parar())