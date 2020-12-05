import pandas as pd
from reportlab.pdfgen import canvas as cv

df = pd.read_csv('Relacao_Produtos.csv')

print(df)