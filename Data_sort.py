import pandas as pd
from openpyxl import load_workbook


file = "Lotofac_hist.xlsx"
excelfile = pd.read_excel(file, sheet_name='Sheet1', engine='openpyxl')
excelfile.drop(excelfile.columns[[0]], axis=1, inplace=True)


def x_last(x):
    ball = 0
    observacoes = []
    if x < 2000:
        ex = excelfile.iloc[:, -x:]
    else:
        ex = excelfile

    for row, rs in ex.iterrows():
        ball += 1
        linha = [element for element in rs if not pd.isnull(element) and not element == '']
        observacoes.append(int(sum(linha) / ball))
    return observacoes


obs = dict()
obs['All long'] = x_last(2115)
obs['Last 200'] = x_last(200)
obs['Last 100'] = x_last(100)
obs['Last 50'] = x_last(50)

excelfile.to_excel(file)

Plan1 = pd.DataFrame(obs, index=range(1, 26))


book = load_workbook(file)
excelfile = pd.ExcelWriter(file, engine='openpyxl')
excelfile.book = book

Plan1.to_excel(excelfile, sheet_name='Plan1')
excelfile.save()
