import random
from time import time, sleep
from libs.PasteSiteParser import PasteSiteParser

service = 'Pasteonline'
pages = ['/archive.php']
viewall = "https://pasteonline.org"
viewpaste = "https://pasteonline.org"
tag = '<a href="'
tag_end = '"'

sw = PasteSiteParser(service, pages, viewall, viewpaste, tag, tag_end)
sw.begin()
