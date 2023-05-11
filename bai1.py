import datetime
import time
import csv
import math
import concurrent.futures

def create_csv_files(input_number, number):
    numbers = [i for i in range(1, number + 1)]
    step = math.ceil(len(numbers)/input_number)

    for i in range(0, len(numbers), step):
        chunk = numbers[i:i+step]
        file_name = f"numbers_{i+1}_{min(i+step, len(numbers))}.csv"
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "number", "time"])
            for j, num in enumerate(chunk):
                id = j + 1
                time = datetime.datetime.now().strftime("%H:%M:%S")
                writer.writerow([id, num, time])

input_number = int(input("Enter a number of csv file: "))
number = int(input("Enter a number of data: "))

#non threadpool
start_time = time.perf_counter()

create_csv_files(input_number, number)

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"Non threadpool execution took {elapsed_time} seconds.")

#with threadpool
start_time = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(create_csv_files, input_number, number)
    result = future.result()

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"Threadpool execution took {elapsed_time} seconds.")