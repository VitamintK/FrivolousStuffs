import os

for file in os.listdir():
    os.rename(file, file.split()[0] + '.' + file.split('.')[-1])
