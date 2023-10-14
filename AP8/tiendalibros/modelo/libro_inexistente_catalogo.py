
from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError


class LibroInexistenteEnCatalogoError(Exception):
    
    def __init__(self, isbn:str):
        self.isbn : str  = isbn

    def __str__(self) -> str:
        return (f"El libro cuyo isbn es: '{self.isbn}' no se encuentra en el catálogo")