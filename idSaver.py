import csv
import time


def save_id(ID, title):
    f = open("ids.csv", "a", newline="")
    to_write = ID, title
    writer = csv.writer(f)
    writer.writerow(to_write)
    f.close()


def read_id(ID):
    row_id = 0
    row_title = "null"

    s_id = str(ID)
    f = open("ids.csv", "r")
    reader = csv.reader(f)

    for row in reader:
        if s_id in row[0]:
            row_id = row[0]
            row_title = row[1]
            time.sleep(2)


    f.close()

    return row_id, row_title



