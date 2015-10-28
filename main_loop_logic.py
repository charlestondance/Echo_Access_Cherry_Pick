__author__ = 'davidmcc'

from save_load import load_csv_array

destination_well_filename = "384lists.csv"
def parse_gui_options(fname, plate_copies, replicates_per_plate):
    SYSTEM_CAPACITY= 5 - plate_copies
    print("hi")
    print(fname)
    print("plate copties " + str(plate_copies) + " replicates per plate" + str(replicates_per_plate))
    data_list, keys = load_csv_array(fname)
    #return a sorted list based on barcode
    newlist = sorted(data_list, key=lambda k: k['BARCODE'])
    dest_list, dest_keys = load_csv_array(destination_well_filename)

    dest_lit_length = len(dest_list) - 1
    print(dest_lit_length)
    dest_list_counter = 0
    dplatecounter = 1
    plate_capacity_checker = 0

    check_barcode = newlist[0]['BARCODE']

    Transfer_volume = 25


    for i in newlist:

        current_barcode = (str(i['BARCODE']))

        if check_barcode == current_barcode:
            continue
        else:
            plate_capacity_checker = plate_capacity_checker + 1
            check_barcode = current_barcode

        if plate_capacity_checker == SYSTEM_CAPACITY:
            print("too much")

        for y in range(0, replicates_per_plate):
            print(str(i) + " " + str(dest_list[dest_list_counter]['Well ID']) + " " + "DP" + str(dplatecounter))
            dict_holder = {"Sample Name": i["FORMATTED_BATCH_ID"], "Source_Plate_Barcode": i["BARCODE"], "SOURCE_WELL_REF": i["WELL_REF"], "DESTINATION_WELL_REF": str(dest_list[dest_list_counter]['Well ID']), "Destnation_Plate_Barcode": "DP" + str(dplatecounter), "Transfer_Volume": Transfer_volume}
            print(dict_holder)
            print(dest_list_counter)
            print()
            dest_list_counter = dest_list_counter + 1
            print(str(dest_list_counter)+ " "+str(dest_lit_length))
            if dest_list_counter > dest_lit_length:
                print("ever in if")
                dest_list_counter = 0
                dplatecounter = dplatecounter + 1
                print("finished")





