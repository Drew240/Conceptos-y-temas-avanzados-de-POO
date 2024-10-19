class Transformador:
    def transformar(self, datos, factor=None):
        
        if factor is None:
            # Si no se proporciona un factor, se calcula la suma
            return sum(datos)
        else:
            # Si se proporciona un factor, se multiplica cada elemento por el factor
            return [x * factor for x in datos]

# Ejemplo de uso:
lista_numeros = [1, 2, 3, 4, 5]

# Sumar los elementos de la lista
suma = Transformador().transformar(lista_numeros)
print("La suma es:", suma)

# Multiplicar los elementos de la lista por 2
resultado_multiplicacion = Transformador().transformar(lista_numeros, 2)
print("La lista multiplicada por 2 es:", resultado_multiplicacion)