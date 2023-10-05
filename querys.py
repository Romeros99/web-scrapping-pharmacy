import csv
from functools import reduce

# Clase en donde se procesan las preguntas (en paradigma funcional)
class Querys:
    _sSeleccion1 = ''
    _sSeleccion2 = ''
    _bListaVacia = True
    _listMedicamentos = []
    _listPrincipiosActivos = []
    _listFarmacias = []
    _masBarato = []
    _masCaro = []
    _precioPromedioCLP = 0
    _precioPromedioUF = 0
    
    # Constructor: Recibe el nombre del csv con los medicamentos y el nombre del txt con los principios activos
    def __init__(self, nombre_csv, nombre_txt):
        listMedicamentos = []

        # Función que convierte a flotantes si es que se puede y los deja en el tipo original en el caso que no se pueda
        def fun2(x):
            try:
                return(float(x))
            except:
                return(x)
    
        # Función que recibe un record (diccionario) con la información de un medicamento, y lo pasa a una lista que se compone
        # de la siguiente manera: [Nombre Farmacia, Nombre Principio Activo, Descripción Medicamento, Precio en CLP, Precio en UF]
        fun = (lambda record: [fun2(record[data]) for data in record])
        with open(nombre_csv, encoding = 'utf8') as csvfile:
            reader = csv.DictReader(csvfile)
            # Se crea una lista de todos los medicamentos usando la función fun
            listMedicamentos = [fun(record) for record in reader]
            
        # Se almacenan los medicamentos, las farmacias y los principios activos en listas
        self._listMedicamentos = listMedicamentos
        self._listFarmacias = ["Cruz Verde", "Farmacias Ahumada", "Salcobrand"]
        text = open(nombre_txt, encoding = 'utf8').read()
        self._listPrincipiosActivos = [line for line in text.split('\n')]
    
    # Getter de propiedades que debemos acceder
    @property
    def sSeleccion1(self):
        return self._sSeleccion1
    
    @property
    def sSeleccion2(self):
        return self._sSeleccion2
    
    @property
    def listMedicamentos(self):
        return self._listMedicamentos
    
    @property
    def listFarmacias(self):
        return self._listFarmacias
    
    @property
    def listPrincipiosActivos(self):
        return self._listPrincipiosActivos
    
    @property
    def bListaVacia(self):
        return self._bListaVacia
    
    # Setter de propiedades que debemos alterar (Selecciones de Farmacia y Principio Activo que se están filtrando)
    @sSeleccion1.setter
    def sSeleccion1(self, sSeleccion1):
        self._sSeleccion1 = sSeleccion1
        
    @sSeleccion2.setter
    def sSeleccion2(self, sSeleccion2):
        self._sSeleccion2 = sSeleccion2

        
    # A continuación, se presentan los métodos escritos en paradigma funcional para realizar las búsquedas específicas
    # Función que imprime los datos de un medicamento
    def printResultado(self, medicamento):
        print("Farmacia: ", medicamento[0])
        print("Principio Activo: ", medicamento[1])
        print("Descripción: ", medicamento[2])
        print("Precio en CLP: ", medicamento[3])
        print("Precio en UF: ", medicamento[4])
        
    # Función que imprime los datos del medicamento más barato
    def getMedicamentoMasBarato(self):
        print("\nResultado:\n")
        self.printResultado(self._masBarato)
    
    # Función que imprime los datos del medicamento más caro
    def getMedicamentoMasCaro(self):
        print("\nResultado:\n")
        self.printResultado(self._masCaro)
        
    # Función que imprime los datos de los precios promedio de los medicamentos
    def getPromedio(self):
        print("\nResultado:")
        print("\nLos remedios buscados tienen un precio promedio de {} CLP ( {} UF )".format(round(self._precioPromedioCLP, 2), round(self._precioPromedioUF, 2)))
        
    # Función que imprime todos los estadísticos de la búsqueda
    def getEstadisticos(self):
        print("\nResultado:")
        print("\nRemedio más barato:")
        self.printResultado(self._masBarato)
        print("\nRemedio más caro:")
        self.printResultado(self._masCaro)
        print("\nLos remedios buscados tienen un precio promedio de {} CLP ( {} UF )".format(round(self._precioPromedioCLP, 2), round(self._precioPromedioUF, 2)))
    
    # Función que Actualiza los atributos del medicamento mas barato, mas caro y los precios promedios para una sub lista
    # que filtra solo los medicamentos pertenecientes a una farmacia en específico (atributo sSeleccion1) y un principio 
    # activo específico (atributo sSeleccion2)
    def preciosFilterFyPA(self):
        # Se genera una sublista en donde se filtra la lista de medicamentos. Se pasan los nombres de las farmacias y principios
        # activos a mayúscula antes de hacer las comparaciones para que no sea case sensitive
        sublist = list(filter(lambda x: x[0].upper() == self.sSeleccion1.upper() and x[1].upper() == self.sSeleccion2.upper(), self.listMedicamentos))
        
        # Se utiliza un try para verificar si hay elementos que satisfacieron la búsqueda
        try:
            # Función lambda dentro del reduce deja el medicamento son el menor precio que, junto con el reduce, realiza
            # las comparaciones en todo el sublist, dejando solo el más barato
            masBarato = reduce(lambda x, y: x if x[3] < y[3] else y, sublist)
            # Simil a masBarato pero buscando el remedio con precio máximo
            masCaro = reduce(lambda x, y: x if x[3] > y[3] else y, sublist)
            # Se suman todos los precios y se divide por la cantidad de remedios en sublist (Promedios) tanto en CLP como en UF
            precioPromedioCLP = reduce(lambda x, y: x + y, [remedio[3] for remedio in sublist])/len(sublist)
            precioPromedioUF = reduce(lambda x, y: x + y, [remedio[4] for remedio in sublist])/len(sublist)
            
            # Se actualizan los atributos correspondientes
            self._masBarato = masBarato
            self._masCaro = masCaro
            self._precioPromedioCLP = precioPromedioCLP
            self._precioPromedioUF = precioPromedioUF
            
            self._bListaVacia = False
        
        except TypeError:
            print("\nNo se encontraron resultados de su búsqueda\n")
            self._bListaVacia = True
    
    # Simil a la función preciosFilterFyPA pero solo filtra por farmacia (sSeleccion1)
    def preciosFilterF(self):
        sublist = list(filter(lambda x: x[0].upper() == self.sSeleccion1.upper(), self.listMedicamentos))
        
        try:
            masBarato = reduce(lambda x, y: x if x[3] < y[3] else y, sublist)
            masCaro = reduce(lambda x, y: x if x[3] > y[3] else y, sublist)
            precioPromedioCLP = reduce(lambda x, y: x + y, [remedio[3] for remedio in sublist])/len(sublist)
            precioPromedioUF = reduce(lambda x, y: x + y, [remedio[4] for remedio in sublist])/len(sublist)

            self._masBarato = masBarato
            self._masCaro = masCaro
            self._precioPromedioCLP = precioPromedioCLP
            self._precioPromedioUF = precioPromedioUF
            
            self._bListaVacia = False
        
        except TypeError:
            print("\nNo se encontraron resultados de su búsqueda\n")
            self._bListaVacia = True
    
    # Simil a la función preciosFilterFyPA pero solo filtra por principio activo (sSeleccion2)
    def preciosFilterPA(self):
        sublist = list(filter(lambda x: x[1].upper() == self.sSeleccion2.upper(), self.listMedicamentos))
        
        try:
            masBarato = reduce(lambda x, y: x if x[3] < y[3] else y, sublist)
            masCaro = reduce(lambda x, y: x if x[3] > y[3] else y, sublist)
            precioPromedioCLP = reduce(lambda x, y: x + y, [remedio[3] for remedio in sublist])/len(sublist)
            precioPromedioUF = reduce(lambda x, y: x + y, [remedio[4] for remedio in sublist])/len(sublist)

            self._masBarato = masBarato
            self._masCaro = masCaro
            self._precioPromedioCLP = precioPromedioCLP
            self._precioPromedioUF = precioPromedioUF
            
            self._bListaVacia = False
        
        except TypeError:
            print("\nNo se encontraron resultados de su búsqueda\n")
            self._bListaVacia = True

    
    # Simil a la función preciosFilterFyPA pero sin filtro, buscando los estadísticos sobre todo el bulto
    def preciosNoFilter(self):
        try:
            masBarato = reduce(lambda x, y: x if x[3] < y[3] else y, self.listMedicamentos)
            masCaro = reduce(lambda x, y: x if x[3] > y[3] else y, self.listMedicamentos)
            precioPromedioCLP = reduce(lambda x, y: x + y, [remedio[3] for remedio in self.listMedicamentos])/len(self.listMedicamentos)
            precioPromedioUF = reduce(lambda x, y: x + y, [remedio[4] for remedio in self.listMedicamentos])/len(self.listMedicamentos)

            self._masBarato = masBarato
            self._masCaro = masCaro
            self._precioPromedioCLP = precioPromedioCLP
            self._precioPromedioUF = precioPromedioUF
            
            self._bListaVacia = False
        
        except TypeError:
            print("\nNo hay medicamentos en la base de datos\n")
            self._bListaVacia = True
     
    # A continuación, se presentan los métodos escritos en paradigma funcional para realizar las búsquedas generales
    # Función que recibe una lista que tiene una farmacia en la primera posición y un principio activo en la segunda.
    # Actualiza los atributos masBarato masCaro y precioPromedioCLP, precioPromedioUF e imprime los estadísticos de esta
    # combinación [farmacia, principio activo]
    def todasCombinacionesFilterFyPA(self, listSelecciones):
        self._sSeleccion1 = listSelecciones[0]
        self._sSeleccion2 = listSelecciones[1]
        
        self.preciosFilterFyPA()
        print("\n-----Estadísticos para Farmacia {} y Principio Activo {}-----\n".format(listSelecciones[0], listSelecciones[1]))
        self.getEstadisticos()
            
    # Función que genera una lista de todas las posibles combinaciones entre farmacias y principios activos y utiliza
    # la función todasCombinacionesFilterFyPA sobre cada una de las combinaciones, mostrando así todos los posibles
    # resultados de estadísticos para las combinaciones de farmacia y principios activos
    def busquedaGeneralFyPA(self):
        [[self.todasCombinacionesFilterFyPA([i, j]) for i in self._listFarmacias] for j in self._listPrincipiosActivos]
    
    # Simil a las dos funciones descritas anteriormente pero filtrando solo por farmacia y por principio activo
    def todasCombinacionesFilterF(self, farmacia):
        self._sSeleccion1 = farmacia
        
        self.preciosFilterF()
        print("\n-----Estadísticos para Farmacia {}-----\n".format(farmacia))
        self.getEstadisticos()
            
    def busquedaGeneralF(self):
        [self.todasCombinacionesFilterF(i) for i in self._listFarmacias]
        
    def todasCombinacionesFilterPA(self, principioActivo):
        self._sSeleccion2 = principioActivo
        
        self.preciosFilterPA()
        print("\n-----Estadísticos para Principio Activo {}-----\n".format(principioActivo))
        self.getEstadisticos()
            
    def busquedaGeneralPA(self):
        [self.todasCombinacionesFilterPA(i) for i in self._listPrincipiosActivos]