from menu import Menu
from querys import Querys

# Se instancia un Menú y un Querys con el csv de medicamentos y el txt de principios activos
menu = Menu()
ask = Querys("ejemplo3.csv", "principios_activos.txt")

# Se inicia el menú
print("Bienvenido a BuscaMed\n\n")

# Función que realiza las operaciones pertinentes dada la selección 1 del usuario
def funcionamiento_menu1(menu, ask):
    if (menu.iSeleccion1 == 1):
        ask.busquedaGeneralF()
    elif (menu.iSeleccion1 == 2):
        ask.busquedaGeneralPA()
    elif (menu.iSeleccion1 == 3):
        ask.busquedaGeneralFyPA()
    elif (menu.iSeleccion1 == 4):
        ask.preciosNoFilter()
        if (ask.bListaVacia == False):
            ask.getEstadisticos()     

# Función que realiza las operaciones pertinentes dada la selección 2 del usuario
def funcionamiento_menu2(menu, ask):
    if (ask.bListaVacia == False):
        if (menu.iSeleccion2 == 1):
            ask.getMedicamentoMasBarato()
        elif (menu.iSeleccion2 == 2):
            ask.getMedicamentoMasCaro()
        elif (menu.iSeleccion2 == 3):
            ask.getPromedio()
        elif (menu.iSeleccion2 == 4):
            ask.getEstadisticos()
            
while (menu.bSeguirMenu):
    # Se abre el menú1
    menu.printMenu1()
    
    # Si la selección del menú1 es 3, se cierra la aplicación
    if (menu.iSeleccion0 == 3):
        print("\nGracias por su preferencia")
        menu.bSeguirMenu = False
        break
    
    # Se abre el menú2
    menu.printMenu2()
    
    # Si la selección del menú1 es 1, se imprimen todas las combinaciones de estadísticos según el filtro seleccionado en menú2
    if (menu.iSeleccion0 == 1):
        funcionamiento_menu1(menu, ask)

    # Si no se seleccionó busqueda general, se abre el menú3 y se le pide los filtros específicos de la búsqueda al usuario
    else:
        menu.printMenu3()
    
        if (menu.iSeleccion1 == 1):
            ask.sSeleccion1 = input("Ingrese el Nombre de la Farmacia: ")
            ask.preciosFilterF()
            funcionamiento_menu2(menu, ask)

        elif (menu.iSeleccion1 == 2):
            ask.sSeleccion2 = input("Ingrese el Nombre del Principio Activo: ")
            ask.preciosFilterPA()
            funcionamiento_menu2(menu, ask)

        elif (menu.iSeleccion1 == 3):
            ask.sSeleccion1 = input("Ingrese el Nombre de la Farmacia: ")
            ask.sSeleccion2 = input("Ingrese el Nombre del Principio Activo: ")
            ask.preciosFilterFyPA()
            funcionamiento_menu2(menu, ask)

        elif (menu.iSeleccion1 == 4):
            ask.preciosNoFilter()
            funcionamiento_menu2(menu, ask)
            
    menu.askSeguirMenu()