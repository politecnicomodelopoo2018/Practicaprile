from Mascota import *
from Vete import *
listaDeDueños = []
listaDeMascotas = []
pepe = Dueño()
pepe.Nombre = "pepe"
jose = Dueño()
jose.Nombre="jose"
listaDeDueños.append(pepe)
listaDeDueños.append(jose)
a = Pajarito("pepe", jose)
listaDeMascotas.append(a)
while True:

    print("1)Agregar Mascota")
    print("2)Borrar Mascota")
    print("3)Modificar Mascota")
    print("4)Agregar Dueño")
    print("5)Alimentar Mascota")
    print("6)Saludar mascota")
    a = input()
    if a == "1":
        print("Seleccione Mascota")
        print("    1)Perro")
        print("    2)Gato")
        print("    3)Pajarito")
        print("    4)Pez")
        b = input()
        if b == "1":
            Nombre = input()
            Dueño = input()
            tu_vieja = []
            mi_vieja_ = []
            for dueño in listaDeDueños:
                tu_vieja.append(dueño.Nombre)
            if Dueño in tu_vieja:
                Dueño = dueño
                nombres = []
                for item in listaDeMascotas:
                    nombres.append(item.Nombre)
                    print(item.Nombre)
                if not Nombre in nombres:
                    c = Perro(Nombre, Dueño)
                    listaDeMascotas.append(c)
                    print("dd")
                    print(c.Saludo)
                else:
                    print("Ya existe una mascota con ese nombre")
            else:
                print("No existe dueño")

        elif b == "2":
            Nombre = input()
            Dueño = input()
            tu_vieja = []
            mi_vieja_ = []
            for dueño in listaDeDueños:
                tu_vieja.append(dueño.Nombre)
            if Dueño in tu_vieja:
                Dueño = dueño
                nombres = []
                for item in listaDeMascotas:
                    nombres.append(item.Nombre)
                    print(item.Nombre)
                if not Nombre in nombres:
                    c = Gato(Nombre, Dueño)
                    listaDeMascotas.append(c)
                    print("dd")
                    print(c.Saludo)
                else:
                    print("Ya existe una mascota con ese nombre")
            else:
                print("No existe dueño")

        elif b == "3":

            Nombre = input()
            Dueño = input()
            Saludo = input()
            tu_vieja = []
            mi_vieja_ = []
            for dueño in listaDeDueños:
                tu_vieja.append(dueño.Nombre)
            if Dueño in tu_vieja:
                Dueño = dueño
                nombres = []
                for item in listaDeMascotas:
                    nombres.append(item.Nombre)
                    print(item.Nombre)
                if not Nombre in nombres:
                    if Saludo != "":
                        c = Pajarito(Nombre, Dueño, Saludo)
                        listaDeMascotas.append(c)
                        print("dd")
                    else:
                        c = Pajarito(Nombre, Dueño)
                        listaDeMascotas.append(c)
                        print("aa")
                else:
                    print("Ya existe una mascota con ese nombre")
            else:
                print("No existe dueño")


        elif b == "4":
            Nombre = input()
            Dueño = input()
            Saludo = ""
            tu_vieja=[]
            mi_vieja_= []
            for dueño in listaDeDueños:
                tu_vieja.append(dueño.Nombre)
            if  Dueño in tu_vieja:
                    Dueño = dueño
                    nombres = []
                    for item in listaDeMascotas:
                        nombres.append(item.Nombre)
                        print(item.Nombre)
                    if not Nombre in nombres:
                        c = Pez(Nombre, Dueño)
                        listaDeMascotas.append(c)
                        print("dd")
                    else:
                        print("Ya existe una mascota con ese nombre")
            else:
                    print("No existe dueño")



    elif a ==


