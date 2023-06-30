import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json

def jsondump(df, name):
    with open(name, "w") as f:
        json.dump(df)

def scrape_table(url, index = 0):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('table')[index]
    df = pd.read_html(str(table))
    df = pd.DataFrame(df[0])
    return df



def df_apply_function(df: pd.DataFrame, colname:str, func):
    # Applies a function to a given column of the dataframe
    df[colname] = df.apply(lambda x: func(x[colname]), axis=1)


cut_initials = ["infogroup -"]
cut_ends = []

def clean_segment_name(name: str):
    name = str(name).strip()
    
    name = name.lower()
    
    # sometimes segment names are enquoted...
    if name[0] == name[-1] == '"':
        name = name[1:-1]

    return name


separator_hierarchy = [
    r">|:|::|-|–|_|\||\(|\)|\[|\]", # > : :: - – _ | ( ) [ ]
    r"/", # /
    r" ", # <space>
    r",", # ,
]

def itemize_segment_name(name: str):

    for sep_re in separator_hierarchy:
        items = re.split(sep_re, name)
         
        if len(items) > 1:
            break
    
    
    items = [i.strip() for i in items]

    items = list(filter(None, items))

    return items