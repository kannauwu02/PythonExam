import csv
import functools
from functools import wraps
import os
from time import sleep

def row_to_dict(row, headers):
    return dict(zip(headers, row))

def print_table(data):
    col_widths = [max(len(str(d[key])) for d in data) for key in data[0].keys()]
    print(" | ".join(key.ljust(w) for key, w in zip(data[0].keys(), col_widths)))
    print("-+-".join("-" * w for w in col_widths))
    for d in data:
        print(" | ".join(str(d[key]).ljust(w) for key, w in zip(d.keys(), col_widths)))

def check_file_size(limit):
    def wrapper(func):
        @wraps(func)
        def inner(file_path):
            size = os.stat(file_path).st_size / 1024
            print(f"The file size in Kilobytes (KB): {size:.2f}")
            if size > limit:
                func(file_path)
            else:
                print(f"The size of the file is smaller than {limit} KB")
        return inner
    return wrapper

@check_file_size(550)
def process_csv_file(file_path):
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        convert_row = functools.partial(row_to_dict, headers=headers)
        data = list(map(convert_row, reader))
        print("Prepare to print...")
        sleep(3)
        print_table(data)

file_path = str(input("Enter the csv file name: "))
process_csv_file(file_path)