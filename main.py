# importing the module
import csv

# open the file in read mode
print("Enter the csv file name:")
name = input()
filename = open('data8.csv', 'r')
filename1= open(name+".csv", 'r')
# creating dictreader object
file = csv.DictReader(filename)
file2 = csv.DictReader(filename1)
# craeting empty lists
month = []
month1 = []
result = []
for col in file:
    month.append(col['ï»¿Full Name'])
    
for col1 in file2:
    month1.append(col1['ï»¿Full Name'])

    
file1 = open(name+".txt","w")

file1.write("Absent student numbers:\n")

month.sort()
month1.sort()

result=(set(month).difference(month1))
     
    
for items in result:
    file1.write('%s\n' %items)
        
file1.close()