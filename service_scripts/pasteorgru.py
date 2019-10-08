"""
Paste.org.ru Parser
"""

import random
from time import time, sleep
from libs.PasteSiteParser import PasteSiteParser

service = 'Pasteorgru'
pages = ['/']
viewall = "http://paste.org.ru"
viewpaste = "http://paste.org.ru/?"
tag = "<a href=\'/?"
tag_end = "\'"

sw = PasteSiteParser(service, pages, viewall, viewpaste, tag, tag_end)
sw.begin()
