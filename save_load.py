import csv

def load_csv_array(filename):
#take a filename and return a list of dicts (containing each row) and list of keys for the dict elements
#read in csv and associate columns to dict keys for each element of list

    with open(filename, newline='') as csvfile:
        read_source = csv.DictReader(csvfile, delimiter=',')

        #get the headers
        headers = read_source.fieldnames

        data_list = []

        print(" ")
        for row in read_source:

            data_list.append(row)



    return(data_list, headers)
