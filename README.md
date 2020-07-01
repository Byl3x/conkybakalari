<h1 align="center">conkybakalari</h1>

<div align="center">
  
  Konfigurace pro conky, která vypisuje průměr známek
  
  ![GitHub](https://img.shields.io/github/license/Byl3x/conkybakalari)
  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Byl3x/conkybakalari)
  ![GitHub last commit](https://img.shields.io/github/last-commit/Byl3x/conkybakalari)
</div>

Průměr z Bakalářů na conky widgetu. conkybakalari je založen na mobilním API bakalářů. Děkuji projektu bakalari-api za dokumentaci.
Prvni spuštění pravděpodobně nebude fungovat, protože se vytváří output soubor, který slouží aby to fungovalo i bez internetu.

## Instalace
Dejte všechny soubory do složky ~/.config/conky/ a zadejte do souboru bakalari.py URL, uživatelské jméno a heslo.
Možná budete muset změnit v conky.conf část, kde se spouští python skript. Musí být spuštěn s Python 3.
(Verzi ověříte spuštěním "python --version", pokud je to verze 2.x.x tak změntě část na python3)

## Možnosti
V souboru conky.conf lze změnit všechno grafické v programu(alignment, font, barva atd.), login se dává do souboru bakalari.py

## Licence
conkybakalari je linencován pod GNU GPLv3

## Dependencies
Všechny dependencies jsou v souboru dependencies.txt(není soubor pro pip), nainstalujte všechny a potom by všechno mělo fungovat.

## Screenshots
![Alt text](https://i.imgur.com/TS2UvKZ.png)
