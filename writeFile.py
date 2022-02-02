import csv

def write(filename, type, question, answer, link, time):
    eachRow = [[type, question, answer, link, time]]
    filename = '%s.csv' % str(filename)

    with open(filename, 'a+', newline='')as f:
        f_csv = csv.writer(f)
        f_csv.writerows(eachRow)
