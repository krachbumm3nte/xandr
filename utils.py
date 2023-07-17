import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json
import numpy as np
from unidecode import unidecode


word_separator = r"( ?[\ \-–_\|\,] ?)"

separator_hierarchy = [
    re.compile(r">|:+| \- | – |\[|\]|\(|\)|\||\,"),  # > : :: - – _ | ( ) [ ]
    re.compile(r"_|-|–|/"),
    # r" ", # <space>
    # r",", # ,
]

useless_segments_re = re.compile("|".join([r"\[null\]",
                                          r"\Atest",
                                          r"[^a-z]+test\Z",
                                          r" test ",
                                          r"\A[a-z0-9]{0,6}\Z", # very short segment names
                                          r"automation\d{5,10}"]))



def jsondump(df, name):
    with open(name, "w") as f:
        json.dump(df, indent=4)


def scrape_table(url, index=0):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('table')[index]
    df = pd.read_html(str(table))
    df = pd.DataFrame(df[0])
    return df


def df_apply_function(df: pd.DataFrame, colname: str, func):
    # Applies a function to a given column of the dataframe
    df[colname] = df.apply(lambda x: func(x[colname]), axis=1)


def clean_segment_name(name: str):
    name = str(name).strip().lower()

    # sometimes segment names are enquoted...
    if name[0] == name[-1] == '"':
        name = name[1:-1]

    return unidecode(name) # remove diactrics and other non-unicode characters



def itemize_segment_name(name: str):
    for sep_re in separator_hierarchy:
        items = re.split(sep_re, name)

        if len(items) > 1:
            break

    items = [i.strip() for i in items] # strip all entries
    items = list(filter(None, items)) # remove empty entries

    return items


def get_eu_names():
    eu_countries = scrape_table(
        "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Country_codes").values
    eu_countries = np.vstack(
        [eu_countries[:, 0:2], eu_countries[:, 2:4], eu_countries[:, 4:6], eu_countries[:-1, 6:8]])
    eu_countries[:, 0] = [countryname.strip().lower()
                          for countryname in eu_countries[:, 0]]  # format all the names
    # remove parentheses from abbreviations
    eu_countries[:, 1] = [countrycode[1:3]
                          for countrycode in eu_countries[:, 1]]
    eu_countries = np.vstack([eu_countries, ["europe", "eu"]])
    return eu_countries
