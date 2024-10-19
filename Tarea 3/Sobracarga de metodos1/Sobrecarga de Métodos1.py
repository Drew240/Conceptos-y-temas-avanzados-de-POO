import math

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def calcular_norma(self, *args):
        
        if len(args) == 2:
            x, y = args
            return math.sqrt(x**2 + y**2)
        elif len(args) == 3:
            x, y, z = args
            return math.sqrt(x**2 + y**2 + z**2)
        else:
            raise ValueError("El vector debe tener 2 o 3 componentes.")

# Ejemplo de uso:
vector2D = Vector(3, 4)
norma2D = vector2D.calcular_norma(vector2D.x, vector2D.y)
print("Norma del vector 2D:", norma2D)

vector3D = Vector(1, 2, 3)
norma3D = vector3D.calcular_norma(vector3D.x, vector3D.y, vector3D.z)
print("Norma del vector 3D:", norma3D)