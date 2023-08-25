from events import get_ufc_events
from results import get_ufc_fight_results
from concurrent.futures import ThreadPoolExecutor
import time
import csv

base_ufc_url: str = 'https://en.wikipedia.org'

if __name__ == "__main__":
    start_time = time.time()

    result_list = [["winner", "loser", "method"]]
    ufc_event_links, ufc_event_data = get_ufc_events()

    for event in ufc_event_data:
        print(event)

    # with ThreadPoolExecutor(max_workers=64) as executor:
    #     results = [executor.submit(get_ufc_fight_results, link) for link in ufc_event_links]

    #     for result in results:
    #         result_list.extend(result.result())

    # csv_file_path = "all_results.csv"

    # with open(csv_file_path, mode="w", newline="") as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     for row in result_list:
    #         csv_writer.writerow(row)

    end_time = time.time()
    print(f"total time execution: {end_time - start_time}")
