import csv

def list_diccionario (csvFile):
    with open(csvFile) as csvFile:
        reader = csv.reader(csvFile, delimiter=(','))
        header = next (reader)
        lista1 = []
        for row in reader:
            dicNew ={key:value for (key,value) in zip(header,row)}
            lista1.append(dicNew)
    
    return lista1

if __name__ == "__main__":
  print(list_diccionario("./WORLD.csv"))

