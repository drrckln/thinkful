import csv

def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))

if __name__ == "__main__":
    csv_path = "TB_data_dictionary_2014-11-01.csv"
    with open(csv_path, "rb") as f_obj:
        csv_reader(f_obj)
