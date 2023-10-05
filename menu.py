from inputI import InputI

# Clase que imprime el menú y recibe las selecciones del usuario mediante variables tipo InputI
class Menu:
    # Atributos
    _iSeleccion0 = InputI(0)
    _iSeleccion1 = InputI(0)
    _iSeleccion2 = InputI(0)
    _iSeleccion3 = InputI(0)
    _bSeguirMenu = True
    
    # Getters de atributos que se desea utilizar en el orquestador
    @property
    def iSeleccion0(self):
        return self._iSeleccion0.intUsuario
    
    @property
    def iSeleccion1(self):
        return self._iSeleccion1.intUsuario
    
    @property
    def iSeleccion2(self):
        return self._iSeleccion2.intUsuario
    
    @property
    def iSeleccion3(self):
        return self._iSeleccion3.intUsuario
    
    @property
    def bSeguirMenu(self):
        return self._bSeguirMenu
    
    # Método que imprime el primer menú y almacena la selección del usuario
    def printMenu1(self):
        print("\n¿Cómo desea obtener los estadísticos?:")
        print("1 - Búsqueda general")
        print("2 - Búsqueda específica")
        print("3 - Cerrar Aplicación\n")
        self._iSeleccion0.setIntUsuarioRestringido(1,3)
        
    # Método que imprime el segundo menú y almacena la selección del usuario
    def printMenu2(self):
        print("\nSeleccione si quiere filtrar su búsqueda:")
        print("1 - Filtrar por Farmacia")
        print("2 - Filtrar por Principio Acivo")
        print("3 - Filtrar por Farmacia y Principio Activo")
        print("4 - Sin Filtrar (Estadísticas del bulto)\n")
        self._iSeleccion1.setIntUsuarioRestringido(1,4)
    
    # Método que imprime el tercer menú y almacena la selección del usuario
    def printMenu3(self):
        print("\n¿Que estadísticas desea buscar?:")
        print("1 - Obtener el Medicamento con Precio Mínimo")
        print("2 - Obtener el Medicamento con Precio Máximo")
        print("3 - Obtener Precio Promedio de Medicamento")
        print("4 - Obtener Todos los Estadísticos\n")
        self._iSeleccion2.setIntUsuarioRestringido(1,4)
    
    # Setter del booleano que termina de mostrar el menú (termina la aplicación)
    @bSeguirMenu.setter
    def bSeguirMenu(self, bSeguirMenu):
        self._bSeguirMenu = bSeguirMenu
        
    # Método que le pregunta al usuario si quiere seguir consultando el menú y realiza los cambios para finalizar
    # la aplicación en caso de  seleccionarlo
    def askSeguirMenu(self):
        print("\n¿Desea realizar otra operación?")
        print("1 - Si")
        print("2 - No")
        self._iSeleccion3.setIntUsuarioRestringido(1,2)
        if (self.iSeleccion3 == 2):
            print("\nGracias por su preferencia")
            self._bSeguirMenu = False
    
    