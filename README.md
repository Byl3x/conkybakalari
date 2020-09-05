<h1 align="center">conkybakalari</h1>

<div align="center">
  
  Konfigurace pro conky, která vypisuje průměr známek a úkoly
  
  ![GitHub](https://img.shields.io/github/license/Byl3x/conkybakalari)
  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Byl3x/conkybakalari)
  ![GitHub last commit](https://img.shields.io/github/last-commit/Byl3x/conkybakalari)
</div>

Průměr a úkoly z Bakalářů na conky widgetu. conkybakalari je založen na mobilním API bakalářů. Použita dokumentace bakalari-api.
conkybakalari může fungovat částečně i offline, pokud nikdo nesmaže xml soubory které si conkybakalari vytvoří, ale samozřejmě neboudou aktualizované známky ani úkoly
!!!Pouze pro bakalari API v1!!!

## Instalace
Dejte všechny soubory do složky ~/.config/conky/ a zadejte do souboru bakalari.py URL, uživatelské jméno a heslo. Pokud složka neexistuje tak ji vytvořte.
Možná budete muset změnit v conky.conf část, kde se spouští python skript. Musí být spuštěn s Python 3.
(Verzi ověříte spuštěním "python --version", pokud je to verze 2.x.x tak změnte část na python3)
Po instalaci můžete dát conky do listu autostart aplikací.

## Možnosti
V souboru conky.conf lze změnit všechno grafické v programu(alignment, font, barva atd.), login se dává do souboru bakalari.py
Filtrování splněných úkolů se dá odstranit v bakalari.py

## Licence
conkybakalari je linencován pod GNU GPLv3

## Dependencies
Všechny dependencies jsou v souboru requirements, nainstalujte všechny, nainstalujte package conky(apt install conky/pacman -S conky, pamac install conky)
Žádná verze pro Windows není a zatím není plánovaná(nemám Windows).
Testováno na distribuci Arch Linux, Manjaro KDE 20.0.3, MX Linux 19.2(Debian) a Slackware 14.2

## Screenshots
![alt text]( https://i.imgur.com/gID4hob.png "Screenshot with transparency")

## Issues
Chyby dávejte sem do Issues nebo posílejte na e-mail mbilek06@gmail.com
