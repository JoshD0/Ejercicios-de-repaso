
from abc import ABC, abstractmethod
from modelo.errores import *

class ReglaValidacion (ABC):
    
    def __init__ (self, _longitud_esperada:int):
        self._longitud_esperada:int = _longitud_esperada
    
    def __init__ (self, _longitud_esperada:int):
        self._longitud_esperada = _longitud_esperada
    
    def validar_longitud (self, clave:str)-> bool:
        if len[clave] > self._longitud_esperada:
            return True
        else:
            raise NoCumpleLongitudMinimaError(f"La clave '{clave}' no cumple con la longitud que se espera = {self._longitud_esperada} ")
        
    def contiene_mayuscula(self, clave:str)-> bool:
        for letra in clave:
            if letra.isupper():
                return True
            else:
                raise NoTieneLetraMayusculaError(f"La clave '{clave}' no contiene ninguna letra mayúscula")

    def contiene_minuscula(self, clave:str)-> bool:
        for letra in clave:
            if letra.islower():
                return True
            else:
                raise NoTieneLetraMinusculaError(f"La clave '{clave}' no copntiene ninguna letra minúscula")

    def contiene_numero(self, clave:str)-> bool:
        for letra in clave:
            if letra.isdigit():
                return True
            else: 
                raise NoTieneNumeroError (f'La clave "{clave}" no contiene ningun numero')
    
    @abstractmethod
    def es_valida(self, clave:str)-> bool:
        pass

class Validador:
    def __init__(self, regla:ReglaValidacion):
        self.regla = regla
    
    def es_valida(self,clave:str)-> bool:
        return self.regla.es_valida(clave)

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self, longitud_esperada:str) -> bool:
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(clave:str) ->bool:
        for letra in clave:
            if letra == "@" or letra == "_" or letra == "#" or letra == "$" or letra == "%":
                return True
            else:
                raise NoTieneCaracterEspecialError(f"La clave '{clave}' no contiene algun caracter especial de tipo: @_#$%")

    def es_valida(self, clave:str)-> bool:
        longitud = self.validar_longitud(clave)
        mayusculas = self.contiene_mayuscula(clave)
        minusculas = self.contiene_minuscula(clave)
        numero = self.contiene_numero(clave)
        caracter_especial = self.contiene_caracter_especial(clave)

        if longitud == True and mayusculas == True and minusculas == True and numero == True and caracter_especial == True:
            return True 
        else:
            raise ValidadorError(f"La clave '{clave}' no cumple la validacion ganimedes")

class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self, longitud_esperada:int):
        super().__init__(longitud_esperada)

    def contiene_calisto (clave:str)-> bool:
        clave_minuscula = clave.lower
        posicion_calisto = clave_minuscula.find("calisto")
        numero_mayusculas = 0
        posicion_final_calisto = posicion_calisto + 7 

        for letra in range (posicion_calisto, posicion_final_calisto, 1):
            if clave[letra].isupper():
                numero_mayusculas += 1 
            
            if numero_mayusculas >= 2 and numero_mayusculas < 7:
                return True
            else:
                raise NoTienePalabraSecretaError(f'la clave "{clave} no contiene la palabra secreta')

    def es_valida(self, clave:str)-> bool:
       longitud = self.validar_longitud(clave)
       numero = self.contiene_numero(clave)
       contiene_calisto = self.contiene_calisto(clave)
       
       if longitud == True and numero == True and contiene_calisto == True:
           return True
       else:
            raise ValidadorError(f"La clave '{clave}' no cumple la valicacion calisto")
