import random
from time import time, sleep
from libs.PasteSiteParser import PasteSiteParser

service = 'Pastelink'
pages = ['/read']
viewall = "https://pastelink.net"
viewpaste = "https://pastelink.net/"
tag = '<a href="'
tag_end = '"'

sw = PasteSiteParser(service, pages, viewall, viewpaste, tag, tag_end)
sw.begin()
