#Week 3 Day 2: File Import Demo #2

#Data File: FileImport_Demo2.txt

#Field1     Field2      FIELD3      FIELD4
#Id No.     Name        Age         Fave Color

#.txt files can be used interchangably with .csv as long as the fields are still separated by commas


#BASE PROGRAM-----------------------------------------------------------------------------------------------------------------


#STEP 1:
import csv

#STEP 2:
total_records = 0

#in this program we will calculate the average age within the fire as well as the total are of all people in file
total_age = 0

#STEP 3:
#with open("C:/User/000778770/Desktop/FileImport_Demo2.txt") as csvfile:
with open("C:/Users/000778770/Desktop/FileImport_Demo2.txt") as csvfile:   
    #STEP 4:
    file = csv.reader(csvfile)
    
    #STEP 5:
    for rec in file:
    
        #STEP 6:
        total_records += 1 #total_records = total_records + 1


        #"trick of the trade" store the rec[#] into vars for easier devolper handling 

        id = rec[0] #first field value is stored into var 'id'
        name = rec[1]
        age = float(rec[2])
        fave_color = rec[3]

        print("{0:5} \t {1:8} \t {2:3} \t {3:7}".format(id, name, age, fave_color))
        
        total_age += age #total_age = total_age + 1
                         # age --> float(rec[2])

#no longer woking in the fire from this line down--------------------------------------------------------


print("\n\nFinished Processing\n\n")
print("\tTOTAL RECORDS: ", total_records)
print("\tTOTAL AGE: {:.2f}".format(total_age))

avg_age = total_age / total_records

print("\tAVERAGE AGE: {:.2f}\n\n\n".format(avg_age))


