__author__ = 'davidmcc'

import csv


SYSTEM_TOTAL_CAPACITY=84
DESTINATION_COPIES=10
SYSTEM_AVAILABLE_CAPACITY = SYSTEM_TOTAL_CAPACITY - DESTINATION_COPIES
HITLIST_FILENAME = "picklist.csv"
DESTINATION_WELLS_FILENAME = "384lists.csv"
output_filename = "Echo_Cherry_pick"
transfer_volume = 25
hitlist_capacity_counter = 1


#read in the hitlist
hitlist_wells = []
with open(HITLIST_FILENAME, newline='') as csvfile:
        read_source = csv.reader(csvfile, delimiter=',')


        for row in read_source:
            #skip first line if header
            if row[0] == 'FORMATTED_BATCH_ID':
                continue

            hitlist_wells.append((row[0], row[1], row[2]))

#read in destination wells
destination_wells = list()
with open(DESTINATION_WELLS_FILENAME, newline='') as csvfile:
    read_source = csv.reader(csvfile, delimiter=',')

    for row in read_source:
        destination_wells.append(row)

def unique_plates(hitlist_wells):
    #this def will return a list of uniqe plates

    #convert to set at sets contain only unique values and are unorderd

    plates = set()

    for row in hitlist_wells:
        plates.add(row[1])

    #convert back to a list so it can be sorted
    plates_list = list(plates)
    plates_list.sort()

    return plates_list

def save_hitlist(hitlist, hitlist_capacity_counter):

    write_name = output_filename + str(hitlist_capacity_counter) + ".csv"

    with open(write_name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        header = "Source Plate Barcode, " + "Sample Name, " + "Transfer Volume, " + "Source Well, " + "Destination Well, " + "Destination Plate Barcode, "
        writer.writerow([header])
        for row in hitlist:
            writer.writerow([row])

def build_picklist_consecutive(SYSTEM_AVAILABLE_CAPACITY, plates, hitlist_wells, destination_wells, hitlist_capacity_counter):

    #reset the loop iterator for the destination wells
    destination_well_counter = 0

    #find the length of the destination wells and subract 1 to get the loop iterator
    destination_wells_length = len(destination_wells) - 1

    #initialise the destination plate number
    destination_plate_number = 1

    current_plate_counter = 0

    madlist =[]

    print(SYSTEM_AVAILABLE_CAPACITY)

    for current_plate in plates:
        print(current_plate)
        print(current_plate_counter)
        for picklist in hitlist_wells:
            if (picklist[1]) == current_plate:
                #create the string for the number of copies
                for i in range(0, DESTINATION_COPIES):
                    madlist.append(str(picklist[1]) + ", " + str(picklist[0]) + ", " + str(transfer_volume) + ", " + str(picklist[2]) + ", " + "Dest" + str(destination_plate_number) + "_" + str(i+1) + ", " +  ", ".join(destination_wells[destination_well_counter]))

                #check you are not at the end of the destination well list for a complete plate
                if destination_wells_length < destination_well_counter + 1:
                    destination_well_counter = 0
                    destination_plate_number = destination_plate_number + 1
                else:

                    destination_well_counter = destination_well_counter + 1

        #check the plate number against the system total capacity
        current_plate_counter = current_plate_counter + 1
        if current_plate_counter == SYSTEM_AVAILABLE_CAPACITY:
            print("fuuuuuul")
            print(madlist)
            save_hitlist(madlist, hitlist_capacity_counter)
            current_plate_counter = 0
            madlist = []
            hitlist_capacity_counter = hitlist_capacity_counter + 1

    save_hitlist(madlist, hitlist_capacity_counter)


plates = unique_plates(hitlist_wells)


build_picklist_consecutive(SYSTEM_AVAILABLE_CAPACITY, plates, hitlist_wells, destination_wells, hitlist_capacity_counter)




