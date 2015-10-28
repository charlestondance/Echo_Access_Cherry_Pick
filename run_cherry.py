__author__ = 'davidmcc'

from save_load import load_csv_array

def open_file_forcherry(fpath):
    load_csv_array(fpath)
    data_list, keys = load_csv_array("picklist.csv")

    print(data_list)
