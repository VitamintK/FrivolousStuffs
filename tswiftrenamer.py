import os

for root, dirs, files in os.walk():
    for file in files:
        os.rename(file, file.split()[0] + '.' + file.split('.')[-1])
