#fichero aplicaciones
__author__ = 'Alumne'
class Aplicaciones():
    def __init__(self,nombre,proveedor,fecha,precio):
        self.fecha = fecha
        self.nombre= nombre
        self.proveedor=proveedor
        self.precio=precio
    def getFecha(self):
        return self.fecha
    def getNombre(self):
        return self.nombre
    def getPrecio(self):
        return self.precio
    def getproveedor(self):
        return self.proveedor
