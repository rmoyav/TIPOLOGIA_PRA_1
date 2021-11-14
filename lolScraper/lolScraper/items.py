###################################################################################################
#
# MODULO: items.py
# DESCRIPCIÓN: Modelo que representa a los datos de un campeón leidos de op.gg.
# AUTOR: Rubén Moya Vázquez
# EMAIL: rmoyav@uoc.edu
#
##################################################################################################

from typing import cast
import scrapy


class Champion(scrapy.Item):
    """[summary]

    Args:
        scrapy ([type]): [description]
    """

    # Servidor del que se han obtenido las estadisticas
    server = scrapy.Field()

    # Nombre del campeón
    name = scrapy.Field()

    # Rol que desempeña en la partida
    position = scrapy.Field()

    # Tier al que pertenece
    tier = scrapy.Field()

    # Ratio de victorias
    win_rate = scrapy.Field()

    # Ratio de victorias
    pick_rate = scrapy.Field()
