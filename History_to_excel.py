import os
import pandas as pd
from selenium import webdriver

wd = webdriver.Chrome("chromedriver.exe")

path = f"file:///{os.path.abspath(os.getcwd())}/lotafac_hist.htm"
wd.get(path)

td_content = []
all_td = []
tr_nodes = wd.find_elements_by_xpath('/html/body/table/tbody/tr')

for tr in tr_nodes[1:]:
    tds = tr.find_elements_by_tag_name('td')[:17]
    if len(tds) == 17:
        for td in tds:
            td_content.append(td.text)

        print(td_content[0])
        result = list(map(int, td_content[2:17]))
        result.sort()
        all_td.append([td_content[1], result.copy()])
        td_content.clear()

wd.close()

file = "Lotofac_hist.xlsx"
table = pd.read_excel(file, engine="openpyxl")

for td in all_td:
    for index in range(1, 26):
        if index > len(td[1]) or td[1][index-1] != index:
            td[1].insert(index - 1, '')
    print(td)
    table[td[0]] = td[1]

table.to_excel(file)
