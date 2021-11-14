###################################################################################################
#
# MODULO: opgg.py
# DESCRIPCIÓN: Este es el spider que efectuará el trabajo de webscraping sobre la web op.gg
# AUTOR: Rubén Moya Vázquez
# EMAIL: rmoyav@uoc.edu
#
###################################################################################################

import scrapy
from lolScraper.items import Champion
from lolScraper.config import *

class OpggSpider(scrapy.Spider):
    """[summary]

    Args:
        scrapy ([type]): [description]

    Yields:
        [type]: [description]
    """

    # Nombre del spider
    name = 'opgg'

    # Dominio al que accederá
    allowed_domains = DOMAINS

    # Servidores a los que accederá
    servers = SERVERS

    # Urls de inicio del crawling
    start_urls = [URL.format(server=x) for x in servers]

    def parse_champions(self, response):
        """
        Esta funcion es la que efectuará la lectura y filtrado de los perfiles de los campeones
        de manera que podamos obtener los atributos que nos interesan

        Args:
            response (Response): La web con el perfil del campeón seleccionado en la request.
        Yields:
            scrapy.items.Champion : El objeto campeon obtenido de filtrar la respuesta.
        """
        
        # Objeto que representa a nuestro campeon.
        champion = Champion()

        champion['server'] = response.url.split('/')[2].split('.')[0]

        # Nombre del campeón
        name = response.xpath(XPATHS_CHAMPION['name']).extract()
        if isinstance(name, list) and name:
            name = name[0]

        champion['name'] = name

        # Rol que desempeña en la partida
        position = response.xpath(XPATHS_CHAMPION['position']).extract()
        if isinstance(position, list):
            position = position[0]
        champion['position'] = position

        # Tier al que pertenece
        champion['tier'] =  response.xpath(XPATHS_CHAMPION['tier']).extract()[0]
        

        rates = response.xpath(XPATHS_CHAMPION['rate']).extract()
        if isinstance(rates, list) and len(rates) == 2:
            # Ratio de victorias   
            champion['win_rate'] =  float(rates[0].split('%')[0])

            # Porcentaje de veces seleccionado
            champion['pick_rate'] =  float(rates[1].split('%')[0])

        yield champion
         
    def parse(self, response):
        """
        Función principal del spider. Su estructura y nombre vienen dados por defecto al crear
        el proyecto con scrapy. Su funcion es recorrer el listado de urls de los campeones y
        llamar a 'parse_champions' con cada respuesta obtenida.

        Args:
            response (Response): La web con el perfil del campeón seleccionado en la request.

        Yields:
            scrapy.Request: La petición a la url de cada campeón.
        """
        champions = response.xpath(STEP).extract()
        for champ in champions:
            yield scrapy.Request(url='https://' + response.url.split('/')[2] + champ, callback=self.parse_champions)
