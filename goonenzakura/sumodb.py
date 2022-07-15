import requests
from bs4 import BeautifulSoup
import rikishi


def get_basho_stats(year: int, month: int) -> list:
    r = requests.get(
        f"https://sumodb.sumogames.de/Query.aspx?show_form=0&columns=1&n_basho=1&show_sansho=on&form1_year={year}&form1_month={month}&form1_m=on"
    )

    if r.status_code != 200:
        raise ValueError(
            f"Query for basho {month}/{year} resulted in HTTP {r.status_code}"
        )

    soup = BeautifulSoup(r.text, "html.parser")
    results = []
    kinboshi = get_kinboshi(year, month)
    for row in soup.find_all("tr"):
        newResult = row.find_all("td")
        if len(newResult) == 4:
            results.append(
                rikishi.Rikishi(
                    newResult[0].string,
                    newResult[2].string,
                    newResult[3].string,
                    kinboshi.count(newResult[0].string),
                )
            )

    return results


def get_kinboshi(year: int, month: int) -> list:
    r = requests.get(
        f"https://sumodb.sumogames.de/scgroup_matrix.aspx?b={year}{str(month).zfill(2)}"
    )

    if r.status_code != 200:
        raise ValueError(
            f"Query for makuuchi results matrix for basho {month}/{year} resulted in HTTP {r.status_code}"
        )

    soup = BeautifulSoup(r.text, "html.parser")
    results = []

    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if "Y" in cells[1].string:
            for cell in row.find_all("img"):
                if "l.gif" in cell.attrs["src"]:
                    results.append(cell.parent.attrs["title"].split(" ")[2])

    return results
