class Navegable:
    def navegar(self):
        return "Navegando en el agua."

class Volador:
    def volar(self):
        return "Volando en el aire."

class Hidroavion(Navegable, Volador):
    pass


hidroavion = Hidroavion()





print(hidroavion.navegar())  
print(hidroavion.volar())   