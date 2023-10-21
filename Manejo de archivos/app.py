
from modelo.datos_metereologicos import DatosMetereologicos


datos = DatosMetereologicos("datos.txt")
print(datos.procesar_datos())