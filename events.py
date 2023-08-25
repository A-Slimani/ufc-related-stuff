import requests
from bs4 import BeautifulSoup
from typing import List

base_wiki_url: str = "https://en.wikipedia.org"


def get_ufc_events() -> (List[str], List[List[str]]):
    url = base_wiki_url + '/wiki/List_of_UFC_events'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    event_links = []
    event_data = []
    past_event_table = soup.find("table", id="Past_events")

    for row in past_event_table.find_all("tr"):
        columns = row.find_all("td")

        if len(columns) >= 2:
            # handle getting the event data
            event_data = [column.get_text(strip=True) for column in columns]
            event_data.append(event_data)

            # handle the links
            event_name_column = columns[1]
            event_name_link = event_name_column.find("a")

            if event_name_link:
                event_link = event_name_link.get("href")
                event_links.append(event_link)

    return event_links, event_data

