import csv


def save_id(ID, title):
    f = open("ids.csv", "a", newline="")
    to_write = ID, title
    writer = csv.writer(f)
    writer.writerow(to_write)
    f.close()


def read_id(ID):
    sID = str(ID)
    f = open("ids.csv", "r")
    reader = csv.reader(f)

    for row in reader:
        if ID in row[0]:
            print(row)

    f.close


read_id(69)
