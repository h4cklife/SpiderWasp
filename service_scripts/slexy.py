"""

Slexy

"""

import sys
import random
from time import time, sleep

sys.path.insert(0, '../libs')
sys.path.insert(1, '../')

from PasteSiteParser import PasteSiteParser

service = 'Slexy'
pages = ['/slexy/recent']
viewall = "https://slexy.org"
viewpaste = "https://slexy.org/view/"
tag = '<a href="/view/'
tag_end = '"'

sw = PasteSiteParser(service, pages, viewall, viewpaste, tag, tag_end)
sw.begin()
