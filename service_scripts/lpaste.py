"""
LPaste Parser
"""

import random
from time import time, sleep
from libs.PasteSiteParser import PasteSiteParser

service = 'Lpaste'
pages = ['/browse?pastes_page=1']
viewall = "http://lpaste.net"
viewpaste = "http://lpaste.net/raw/"
tag = '<a href="/'
tag_end = '"'



sw = PasteSiteParser(service, pages, viewall, viewpaste, tag, tag_end)
sw.begin()
