import os

for index, file in enumerate(os.listdir()):
    os.rename(file, str(index) + '.' + file.split('.')[-1])
