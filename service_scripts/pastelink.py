"""

PasteLink

"""

import sys
import random
from time import time, sleep

sys.path.insert(0, '../libs')
sys.path.insert(1, '../')

from PasteSiteParser import PasteSiteParser

service = 'Pastelink'
pages = ['/read']
viewall = "https://pastelink.net"
viewpaste = "https://pastelink.net/"
tag = '<a href="'
tag_end = '"'

sw = PasteSiteParser(service, pages, viewall, viewpaste, tag, tag_end)
sw.begin()
