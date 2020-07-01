#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bakalari.py
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
url = "<url>"
token = bakalari_token.generate_token(url, "<username>", "<password>")
r = requests.get(url+"?hx="+token+"&pm=znamky")
r2 = requests.get(url+"?hx="+token+"&pm=ukoly")

requeststr = str(r.text)
requeststr2 = str(r2.text)

gradexml = open("znamky.xml", "w")
gradexml.write(requeststr)
gradexml.close()

hwxml = open("ukoly.xml", "w")
hwxml.write(requeststr2)
hwxml.close()

mygrade = minidom.parse('znamky.xml')
myhomework = minidom.parse('ukoly.xml')
ukolypredmety = myhomework.getElementsByTagName('predmet')
ukolypopisy = myhomework.getElementsByTagName('popis')
ukolystatusy = myhomework.getElementsByTagName('status')
prumery = mygrade.getElementsByTagName('prumer')
predmety = mygrade.getElementsByTagName('nazev')

prumer = []
predmet = []
ukolypopis = []
ukolypredmet = []
ukolystatus = []

for elem in ukolypopisy:
    ukolypopis.append(elem.firstChild.data)
for elem in ukolypredmety:
    ukolypredmet.append(elem.firstChild.data)
for elem in ukolystatusy:
	ukolystatus.append(elem.firstChild.data)
	
for elem in prumery:
    prumer.append(elem.firstChild.data)
for elem in predmety:
    predmet.append(elem.firstChild.data)

ukolycombined = ""
combined = ""
i = 0
l = 0

while len(prumer) > i:
	combined = combined+predmet[i]+": "+prumer[i]+"\n"
	i += 1
print(combined)

while len(ukolypopis) > l:
	if ukolystatus[l] == "probehlo":
		l += 1
	else:
		ukolycombined = ukolycombined+ukolypredmet[l]+": \n"+ukolypopis[l]+" \n"+"Status:"+ukolystatus[l]+"\n"
		ukolycombined = ukolycombined.replace("<br />", " \n")
		l += 1
print(ukolycombined)
