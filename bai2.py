import csv
import functools

def row_to_dict(row, headers):
    return dict(zip(headers, row))

def print_table(data):
    col_widths = [max(len(str(d[key])) for d in data) for key in data[0].keys()]
    print(" | ".join(key.ljust(w) for key, w in zip(data[0].keys(), col_widths)))
    print("-+-".join("-" * w for w in col_widths))
    for d in data:
        print(" | ".join(str(d[key]).ljust(w) for key, w in zip(d.keys(), col_widths)))

with open("test_modified.csv", "r") as f:
    reader = csv.reader(f)
    headers = next(reader)
    convert_row = functools.partial(row_to_dict, headers=headers)
    data = list(map(convert_row, reader))

print_table(data)