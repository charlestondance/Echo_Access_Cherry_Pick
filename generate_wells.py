__author__ = 'davidmcc'

row_letter = "A"

column_number = 1

wells_list = []

for i in range(ord(row_letter), ord("P")+1):
    for p in range(column_number, 22+1):
        if p < 10:
            wells_list.append(chr(i) + "0" + str(p))
        else:
            wells_list.append(chr(i) + str(p))

print(wells_list)