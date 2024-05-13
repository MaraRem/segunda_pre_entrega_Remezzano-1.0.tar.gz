
class Cliente():
    def __init__(self,nombre,apellido,cuit,localidad):
        self.nombre = nombre
        self.apellido = apellido
        self.cuit = cuit
        self.localidad = localidad
           
    def compra(self,nuevo_articulo):
        self.nuevo_articulo = nuevo_articulo
        return f'Hola, soy el cliente: {self.nombre} {self.apellido} y estoy comprando: {nuevo_articulo}.'

    def paga(self):
        return f'Estoy pagando mis productos comprados soy {self.nombre} de {self.localidad}'

    def consulta(self,articulo):
        self.consulta_art = articulo
        return f'{self.nombre} {self.apellido} consulta...Tienen stock del articulo {articulo}'
    
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"






