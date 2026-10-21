# rows = load_rows("data/points.csv")
import csv

def load_rows(data_name):
    with open(data_name, mode='r',) as data:
        reader = csv.reader(data, delimiter=',')
        next(reader)

        data_list = []
        for row in reader:
            val1 = float(row[1])
            val2 = float(row[2])
            data_list.append((row[0], val1, val2))

    return data_list
