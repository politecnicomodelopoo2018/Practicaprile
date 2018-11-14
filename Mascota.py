class Dueño(object):
    Nombre = None

class Mascota(object):
    Nombre = None
    Saludo = None
    Dueño = None

    def saludar(self,persona):

        if (self.Dueño == persona):
            return self.Saludo
        return self.Saludo.upper()+'!'
    def __init__(self,nombre,dueño):
        self.Nombre = nombre
        self.Dueño = dueño

class Perro(Mascota):

    Saludo = "Guau"

class Gato(Mascota):

    Saludo = "Miau"

class Pajarito(Mascota):

    Saludo = " "

    def __init__(self,nombre,dueño,saludo="Pio"):

        Mascota.__init__(self,nombre,dueño)
        self.Saludo = saludo

    def saludar(self,persona):

        if self.Dueño == persona:
            return self.Saludo
        return " "

class Pez(Mascota):

    Vidas = 10

    def alimentar(self):

        self.Vidas += 1

    def saludar(self,persona):
        if persona == self.Dueño:

            self.Vidas -= 1
            return False

        return True