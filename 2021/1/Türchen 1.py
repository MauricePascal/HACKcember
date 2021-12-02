"""
Die Aufgabe des Türchen ist es, eine 2021x .zip-verpackte Datei so oft zu entpacken,
bis man die Ursprungstextdatei hat, in der das Passwort für das Video steht.

Video von Algorithmen verstehen: https://www.youtube.com/watch?v=G3vLQP5yAKQ
Artikel: https://www.floriandalwigk.de/santas-geschenk-hackcember-1

Erstellt am 01.12.2021 (dd.MM.yyyy) mit PyCharm Community

Mit freundlichen Grüßen
Maurice-Pascal
"""

import zipfile
import os

index = 0

for x in range(2021):
    if index == 0:
        with zipfile.ZipFile(f"D:\\Development and Engineering\\Python\\HACKcember\\2021\\1\\geschenk.zip",
                             'r') as zip_ref:
            zip_ref.extractall(f"D:\\Development and Engineering\\Python\\HACKcember\\2021\\1\\unzipped\\{index}")
            index += 1
    else:
        files = os.listdir(f"D:\\Development and Engineering\\Python\\HACKcember\\2021\\1\\unzipped\\{index - 1}")
        for file in files:
            with zipfile.ZipFile(f"D:\\Development and Engineering\\Python\\HACKcember\\2021\\1\\unzipped\\{index - 1}\\{file}",
                                 'r') as zip_ref:
                zip_ref.extractall(f"D:\\Development and Engineering\\Python\\HACKcember\\2021\\1\\unzipped\\{index}")
                index += 1