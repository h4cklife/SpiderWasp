"""

JustPasteIt

"""

import sys
import random
from time import time, sleep

sys.path.insert(0, '../')

from libs.PasteSiteParser import PasteSiteParser

service = 'Justpasteit'
pages = ['/top', '/top/day/new']
viewall = "https://justpaste.it"
viewpaste = "https://justpaste.it/"
tag = "<a href='"
tag_end = "'"


sw = PasteSiteParser(service, pages, viewall, viewpaste, tag, tag_end)
sw.begin()
