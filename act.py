# Andre Marroquin Tarot- 22266
# Sergio Orellana- 221122
# Brandon Reyes- 22992
# Andy Fuentes - 22944
# Davis Roldán - 22672

import re
import csv

# Función para leer el contenido de una página web desde un archivo local
def leerPaginaWeb(archivoPagina):
    with open(archivoPagina, 'r', encoding='utf-8') as archivo:
        return archivo.read()

# Análisis del contenido HTML para obtener productos y sus imágenes
def analizarHtmlYExtraerDatos(contenidoHtml):
    expresionRegular = re.compile(r'<div class="caption col-12">.*?<p class="pr-4">(.*?)</p>.*?<div class="overflow-hidden".*?<img.*?src="(.*?)"', re.DOTALL)
    listaProductos = expresionRegular.findall(contenidoHtml)
    return listaProductos

# Guarda los datos extraídos en un archivo CSV
def guardarEnCsv(datosProductos, nombreArchivo):
    with open(nombreArchivo, 'w', newline='', encoding='utf-8') as archivoCsv:
        manejadorCsv = csv.writer(archivoCsv)
        # Encabezados del archivo CSV
        manejadorCsv.writerow(['Nombre del Producto', 'URL de la Imagen'])  
        manejadorCsv.writerows(datosProductos)  # Datos de productos

# Inicia el proceso de carga, análisis y guardado
contenidoPagina = leerPaginaWeb('pagina.html')
productosEncontrados = analizarHtmlYExtraerDatos(contenidoPagina)
guardarEnCsv(productosEncontrados, 'listadoProductos.csv')

print("CSV creado")
