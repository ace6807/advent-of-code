import requests
from bs4 import BeautifulSoup


def get_title_for_day(day: int, year: int = 2022) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    return soup.article.h2.string.strip("- ")
