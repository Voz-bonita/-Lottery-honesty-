import pandas as pd
from openpyxl import load_workbook


file = "Lotofac_hist.xlsx"
excelfile = pd.read_excel(file, sheet_name='Sheet1', engine='openpyxl')
excelfile.drop(excelfile.columns[[0]], axis=1, inplace=True)


def last_x(x):
    ball = 0
    observacoes = []

    ex = excelfile.iloc[:, -x:]
    for row, rs in ex.iterrows():
        ball += 1
        linha = [element for element in rs if not pd.isnull(element) and not element == '']
        observacoes.append(int(sum(linha) / ball))
    return observacoes


all_long = len(excelfile.columns)
obs = dict()
obs['Obs_value'] = last_x(all_long)
obs['Exp_value'] = (all_long * 15/25)

excelfile.to_excel(file)

Plan1 = pd.DataFrame(obs, index=range(1, 26))


book = load_workbook(file)
excelfile = pd.ExcelWriter(file, engine='openpyxl')
excelfile.book = book

Plan1.to_excel(excelfile, sheet_name='Plan1')
excelfile.save()
