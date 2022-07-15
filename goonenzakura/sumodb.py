import requests
from bs4 import BeautifulSoup
import rikishi


def get_basho_stats(year: int, basho: int) -> list:
    r = requests.get(
        f"https://sumodb.sumogames.de/Query.aspx?show_form=0&columns=1&n_basho=1&show_sansho=on&form1_year={year}&form1_month={basho}&form1_m=on"
    )
    soup = BeautifulSoup(r.text, "html.parser")
    results = []
    for row in soup.find_all("tr"):
        newResult = row.find_all("td")
        if len(newResult) == 4:
            results.append(
                rikishi.Rikishi(
                    newResult[0].string, newResult[2].string, newResult[3].string
                )
            )

    return results
