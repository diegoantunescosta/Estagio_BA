import pandas as pd
import matplotlib.pyplot as plt
import re
#Buscando arquivo
df = pd.read_csv('checkout_business_information_limpo.csv')
print (df)
teste = ' sadaf sada@das.com'
split_term = '@'
resultado = re.split(split_term, df)
print (resultado)



