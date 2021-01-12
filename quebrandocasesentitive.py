import pandas as pd
import matplotlib.pyplot as plt
#Buscando arquivo
df = pd.read_csv('checkout_business_information_limpo.csv')
texto = state ['state']
texto_quebrado = textos.str.lowe().str.split()
palavras = set()
for palavra in texto_quebrado:
    palavras.update(palavra)

print (palavra)