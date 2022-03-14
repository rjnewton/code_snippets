#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
from os import listdir
from os.path import isfile, join, dirname, realpath
import re
from PIL import Image,ImageDraw,ImageFont

filter = "fonts.*"
dname = dirname(realpath(__file__))
print (f"dirname: {dname}")
fontfiles = [f for f in listdir(dname) if isfile(join(dname, f)) and re.search(filter,f)]

print (fontfiles)
