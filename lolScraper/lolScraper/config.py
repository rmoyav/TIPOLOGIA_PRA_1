
###################################################################################################
#
# MODULO: config.py
# DESCRIPCIÓN: Este modulo contiene parametros de configuración del spider, tales como
# las expresiones regulares a utilizar para encontrar los datos deseados de un campeón.
# AUTOR: Rubén Moya Vázquez
# EMAIL: rmoyav@uoc.edu
#
###################################################################################################

DOMAINS = ["op.gg"]
SERVERS = ['br', 'eune', 'euw', 'jp', 'lan', 'las', 'na', 'oce', 'ru', 'tr', 'www']
URL = "https://{server}.op.gg/champion/statistics/"
STEP ='//a//@href[contains(.,"statistics")]'

XPATHS_CHAMPION = {
    'name': '//h1[@class="champion-stats-header-info__name"]/text()',
    'position': '//span[@class="champion-stats-header__position__role"]/text()',
    'tier': './/div[@class="champion-stats-header-info__tier"]/b/text()',
    'rate': '//div[@class="champion-stats-trend-rate"]/text()'
}
