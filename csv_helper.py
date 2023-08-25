import csv
from typing import List


def save_to_csv(filepath: str, data: str):
    with open(filepath, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)


def save_to_csv_list(filename: str, directory: str, data: List[str]):
    pass
