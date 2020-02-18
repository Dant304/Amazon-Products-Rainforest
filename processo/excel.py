import xlwt as xw
from processo.produtos import pegarDados
    
wb = xw.Workbook()
ws = wb.add_sheet("PRODUTOS AMAZON")

def criarTabela():
    ws.write(0,0,'PRODUTO')
    ws.write(0,1,'PREÇO')
    
def inserirDados():
    cont = 1
    produtos = pegarDados()
    while cont <= len(produtos):
        ws.write(cont,0,produtos['search_results'][cont]['title'])
        precos = produtos['search_results'][cont]['prices']
        ws.write(cont,1,precos[0]['value'])
        cont+= 1

def salva():
    wb.save('produtos2.xls')