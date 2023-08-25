import requests
from bs4 import BeautifulSoup

base_ufc_url: str = 'https://en.wikipedia.org'


def get_ufc_fight_results(link: str):
    result = []
    url = base_ufc_url + link
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find("table", class_="toccolours")

    for row in table.find_all("tr"):
        columns = row.find_all("td")
        if len(columns) >= 3:
            fight_winner = columns[1].get_text(strip=True)
            fight_loser = columns[3].get_text(strip=True)
            method = columns[4].get_text(strip=True)
            result.append([
                 fight_winner,
                 fight_loser,
                 method
            ])
    print(f"{link} completed")
    print(result)
    return result






