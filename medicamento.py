
class Medicamento():
  _principioactivo = None
  _farmacia = None
  _descripcion = None
  _precio = None
  _precio_en_UF = None

  def __init__(self,farmacia, principioactivo, descripcion, precio, UF_hoy):
    self.principioactivo = principioactivo
    self.farmacia = farmacia
    self.descripcion = descripcion
    self.precio = precio
    self.precio_en_UF= round(precio/UF_hoy,2)

  
  @property
  def principioactivo (self):
    return self._principioactivo
  
  @principioactivo.setter
  def principioactivo(self, principioactivo):
    self._principioactivo = principioactivo
  
  @property
  def farmacia(self):
    return self._farmacia
  
  @farmacia.setter
  def farmacia(self, farmacia):
    self._farmacia = farmacia

  @property
  def descripcion(self):
    return self._descripcion
  
  @descripcion.setter
  def descripcion(self, descripcion):
    self._descripcion = descripcion

  @property
  def precio(self):
    return self._precio
  
  @precio.setter
  def precio(self, precio):
    self._precio = precio
  

  







