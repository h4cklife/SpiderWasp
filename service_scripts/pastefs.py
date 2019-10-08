import random
from time import time, sleep
from libs.PasteSiteParser import PasteSiteParser

service = 'Pastefs'
pages = ['/recent.php', '/trends.php']
viewall = "https://www.pastefs.com"
viewpaste = "https://www.pastefs.com/pid/"
tag = "href=\'https://www.pastefs.com/pid/"
tag_end = "\'"


sw = PasteSiteParser(service, pages, viewall, viewpaste, tag, tag_end)
sw.begin()
