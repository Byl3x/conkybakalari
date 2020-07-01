#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bakalari.py
#  
#  Copyright 2020 Unknown <bylex@mx>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import requests
import bakalari_token
from xml.dom import minidom
url = ""
token = bakalari_token.generate_token(url, "", "")
r = requests.get(url+"?hx="+token+"&pm=znamky")

requeststr = str(r.text)

f = open("request.xml", "w")
f.write(requeststr)
f.close()

mydoc = minidom.parse('request.xml')
prumery = mydoc.getElementsByTagName('prumer')
predmety = mydoc.getElementsByTagName('nazev')
prumer = []
predmet = []
for elem in prumery:
    prumer.append(elem.firstChild.data)
for elem in predmety:
    predmet.append(elem.firstChild.data)
combined = ""
i = 0
clear = open("./output", "w")
clear.write("")
clear.close()
output = open("./output", "a")

while len(prumer) > i:
	combined = predmet[i]+": "+prumer[i]+"\n"
	i += 1
	output.write(combined)
