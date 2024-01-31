import pandas as pd

bigData =pd.read_excel("vendas.xlsx")


os10Primeiros=bigData.head(10)
qtdLinhasxColunas=bigData.shape
info=bigData.info
preco=bigData.preco
descricao=preco.describe()
qtdVendasLoja=bigData.loja.value_counts()
qtdVendasCidade=bigData.cidade.value_counts()
qtdVendasPg=bigData.forma_pagamento.value_counts()
faturamentoPorLoja=bigData.groupby("lojas").preco.sum()
faturamentoPorCidade=bigData.groupby("")
print(qtdVendasPg)