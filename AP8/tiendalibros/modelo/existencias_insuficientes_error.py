from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):


    # Defina metodo inicializador
    def __init__(self, libro: Libro, cantidad_a_comprar:int):
        super().__init__(libro)
        self.cantidad_a_comprar : int = cantidad_a_comprar
    # Defina metodo espcial
    def __str__(self) -> str:
        return (f"El libro titulado '{self.libro.titulo}' cuyo isbn es '{self.libro.isbn}' no tiene las existencias suficientes, la cantidad a comprar es: {self.cantidad_a_comprar}, y las existencias actuales son: {self.libro.existencias}")
