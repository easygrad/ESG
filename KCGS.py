from typing import ItemsView
import requests
import re
import pandas as pd
import seaborn as sns
from io import BytesIO
from tqdm import tqdm
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

for year in range(2011, 2021):
    url="http://www.cgs.kr/business/esg_tab04.jsp?pg=1&pp=10&&sfyear={year}&sgrade=#ui_contents".format(year=year)
    res=requests.get(url, headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")
    item_table=soup.find("div", attrs={"class":"business_board"})
    item_cnt=item_table.find("em").get_text()

    url_f="http://www.cgs.kr/business/esg_tab04.jsp?pg=1&pp={item_cnt}&&sfyear={year}&sgrade=#ui_contents".format(item_cnt=item_cnt, year=year)
    res_f=requests.get(url_f, headers=headers)
    res_f.raise_for_status()
    html=BytesIO(res_f.content)
    dataset_year=pd.read_html(html)[0]
    if year==2011:
        dataset=dataset_year
    else:
        dataset=pd.concat([dataset, dataset_year])

print(dataset)
dataset.to_csv("ESG_Ratings_KCGS.csv", encoding="euc-kr")