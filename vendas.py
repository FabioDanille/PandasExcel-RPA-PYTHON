import os
from pathlib import Path
import pandas as pd

caminho = Path.cwd()
vendas = pd.DataFrame(columns=['Loja','Vendedor','Valor da Venda'])

for pasta in caminho.iterdir():
    if pasta.is_dir():
        os.chdir(pasta)
        caminho = Path.cwd()
        for pasta in caminho.iterdir():
            if pasta.is_dir():
                os.chdir(pasta)
                caminho = Path.cwd()
                for pasta in caminho.iterdir():
                    if pasta.is_dir():
                        os.chdir(pasta)
                        caminho = Path.cwd()
                        for pasta in caminho.iterdir():
                            if pasta.is_dir():
                                os.chdir(pasta)
                                caminho = Path.cwd()
                                for arquivo in caminho.iterdir():
                                    venda = pd.read_excel(arquivo)
                                    vendas = vendas.append(venda, ignore_index=True)

vendas_agregado = vendas.groupby(by="Loja").sum()
del vendas_agregado['Vendedor']
os.chdir(r'C:\Users\fabio\OneDrive\Documentos\TI\1-PROJETOS-PYTHON\ExcelPandas\Vendas')
vendas_agregado.to_excel("Vendas por Loja.xlsx")

print (pd.read_excel("Vendas por Loja.xlsx"))