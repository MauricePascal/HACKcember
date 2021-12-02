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