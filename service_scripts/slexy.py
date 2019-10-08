import random
from time import time, sleep
from libs.PasteSiteParser import PasteSiteParser

service = 'Slexy'
pages = ['/slexy/recent']
viewall = "https://slexy.org"
viewpaste = "https://slexy.org/view/"
tag = '<a href="/view/'
tag_end = '"'

sw = PasteSiteParser(service, pages, viewall, viewpaste, tag, tag_end)
sw.begin()
