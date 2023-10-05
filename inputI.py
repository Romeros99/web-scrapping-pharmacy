# Clase que recibe enteros y valida que el input sea tipo entero, junto con validar restricciones de mínimo
# y máximo para el input
class InputI:
    _intUsuario = 0
    
    def __init__(self, intUsuario = 0):
        self._intUsuario = intUsuario
            
    @property
    def intUsuario(self):
        return self._intUsuario
    
    def setIntUsuarioRestringido(self, minR, maxR):
        selUsuario = input("\nIngrese un número entre el {} y el {}: ".format(minR, maxR))
        try:
            intUsuario = int(selUsuario)
            if (int(selUsuario) < minR or int(selUsuario) > maxR):
                raise AttributeError
            self._intUsuario = int(selUsuario)
        except AttributeError as e:
            print("Número fuera de rango. Debe estar entre {} y {}".format(minR, maxR))
            self.setIntUsuarioRestringido(minR, maxR)
            return
        except ValueError as e:
            print("El número ingresado no es válido")
            self.setIntUsuarioRestringido(minR, maxR)
            return
