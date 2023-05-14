import datetime
import time
import csv
import math

def generate_numbers(number):
    return [i for i in range(1, number + 1)]

def split_numbers(numbers, input_number):
    step = math.ceil(len(numbers) / input_number)
    return [numbers[i:i + step] for i in range(0, len(numbers), step)]

def create_csv_files(input_number, number):
    numbers = generate_numbers(number)
    chunks = split_numbers(numbers, input_number)

    for i, chunk in enumerate(chunks):
        start = chunks.index(chunk) * len(chunks[0]) + 1
        end = min(start + len(chunk) - 1, number)
        file_name = f"numbers_{start}_{end}_nopool.csv"
        write_csv_file(file_name, chunk)

def write_csv_file(file_name, chunk):
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "number", "time"])
        for j, num in enumerate(chunk):
            id = j + 1
            current_time = datetime.datetime.now().strftime("%H:%M:%S:%f")
            writer.writerow([id, num, current_time])

def main():
    input_number = int(input("Enter the number of CSV files to create: "))
    number = int(input("Enter the number of data: "))

    start_time = time.perf_counter()
    create_csv_files(input_number, number)
    end_time = time.perf_counter()
    print(f"Non-threadpool execution took {end_time - start_time} seconds.")

if __name__ == "__main__":
    main()
