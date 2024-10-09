from csv import DictReader
with open("data.csv","r") as filee:
    document =  DictReader(filee, delimiter=';', quotechar='"')
    for dila in filee:
        print(dila)


