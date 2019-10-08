"""

Pastie

"""

import sys
import random
from time import time, sleep

sys.path.insert(0, '../')

from libs.PasteSiteParser import PasteSiteParser

service = 'Pastie'
pages = ['/lists', '/trends']
viewall = "https://pastie.ru"
viewpaste = "https://pastie.ru/view/"
tag = '<a href="'
tag_end = '"'

sw = PasteSiteParser(service, pages, viewall, viewpaste, tag, tag_end)
sw.begin()
