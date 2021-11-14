# Práctica 1: Web scraping

Este proyecto se corresponde a la primera *PRA* de la asignatura **Tipología y ciclo de vida de los datos** del **Máster en Ciencia de Datos** de la **UOC**.

## Descripción

En esta primera practica se desea generar un dataset con información explotable obtenido a partir de la utilización de técnicas de web scraping. Para nuestro caso concreto, nos hemos centrado en el sector de los eSports (más concretamente, en el juego League of Legends) por aunar dos aspectos relevantes a la hora de realizar esta práctica. En primer lugar, cabe destacar el volumen de datos disponibles en distintas páginas dedicadas al juego, lo cual ofrece grandes oportunidades a nivel de explotación y análisis de datos. Posteriormente, hay que tener en cuenta que los eSports son un sector en auge y muy voluble en el que el análisis derivado de los procesos de ciencia de datos puede decantar el resultado de una competición.

Para realizar nuestro dataset hemos decidido obtener los datos de la web **https://op.gg/**, posiblemente, la web más completa a nivel de información explotable centrada en League of Legends.

## Miembros del equipo
La práctica ha sido realizada por completo por el alumno **Rubén Moya Vázquez**.

## Ficheros del proyecto.
En este apartado cabe destacar que hay dos tipos de ficheros: Los generados automáticamente por scrapy al crear el proyecto (y que no han sido modificados) y los que contienen código desarrollado por los miembros del equipo. En esta lista referenciaremos solamente los últimos:

1. **README.md**: Este fichero que describe el proyecto de manera superficial.
2. **config.py**: Fichero con constantes de configuración del spider.
3. **items.py**: Fichero que contiene el modelo de nuestras entidades a extraer.
4. **opgg.py**: Fichero que contiene nuestro spider, con el que leeremos los datos de las diferentes páginas de la web.
5. **settings.py**: Fichero de configuración en el que se ha modificado el agente para poder extraer los datos.
6. **champions.csv**: El dataset obtenido en formato csv.

## Ejecución
Para la construcción de este proyecto se ha utilizado el framework de webscraping **scrapy**. Si no se tiene dicho framework instalado en el entorno python se debe instalar con el siguiente comando:

``pip install scrapy``

Para ejecutar el spider y que obtenga los datos deseados se debe ejecutar el siguiente comando desde el directorio del proyecto:

``scrapy crawl opgg -o champions.csv``