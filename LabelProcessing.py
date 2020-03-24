import csv

path = 'data/data.csv'

#returns a list of rows to make it easier to parse
def csv_reader(path):

    titles = []
    rows = []

    with open(path, 'r') as file:

        #creating a csv reader object
        csvreader = csv.reader(file)

        #extracting field names through first row
        titles = csvreader.next()

        #extracting each data row one by one
        for row in csvreader:
            rows.append(row)

    return rows

#function that will split the labels in each diagnosis given an image_name with the extension returns a list of split labels
def Label_parser(image_name):
    rows = csv_reader(path)

    #row[0] = image name
    #row[1] = diagnosis
    for row in rows:

        if(row[0] == image_name):
            tmp = ''.join(row[1]) #change type to string in order to split
            tmp = tmp.split('|')

    return tmp #returns parsed label



#testing purposes

name = "00000001_001.png"
name1 = "00000013_030.png"
name2 = '00000031_000.png'
name3 = '00000032_012.png'

print(Label_parser(name1))
