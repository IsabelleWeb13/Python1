# test variables
# Lab 8: Composite Data Type
# imprimer des données se trouvant sur un fichier .csv 

import csv
import copy

#Exercise 1: Car Inventory

# Define a dictionary to hold our data.
#Définir un dictionnaire pour contenir nos données. 
# --------------------------------------------TITRES DU FICHIER .CSV : 
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
    }

# Print out the initial key and values.
# -------------------------------------------VA IMPRIMER LES TITRES ET LES VALEURS PAR DEFAUT
print("TITRES ET VALEURS PAR DEFAUT------------------------------------------")
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))




    # Define an empty list to keep a copy in memory.
myInventoryList = []
# Read the inventory from the csv file.
# créer un fichier car_fleet.csv avant
with open('car_fleet.csv') as csvFile:
#with open('car_fleet.xlsx') as xlsxFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    print ("\n")
    print("TITRES ET DONNEES EN COLONNE------------------------------------------")
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f'Processed {lineCount} lines.')
    print ("\n")
    print("TITRES ET DONNEES EN FORMULAIRE ------------------------------------------")
    # Print the inventory from the copy in memory.
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
       print("{} : {}".format(key,value))
    print("-----")

