import requests
import time
from time import perf_counter_ns


def measure_round_trip_time(url):
    try:
        start_time = perf_counter_ns()
        response = requests.get(url)
        end_time = perf_counter_ns()
        round_trip_time = end_time - start_time
        return round_trip_time
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for d in data:
            file.write(str(d) + '\n')
