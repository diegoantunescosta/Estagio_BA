import pandas as pd
import matplotlib.pyplot as plt
#Buscando arquivo
df = pd.read_csv('checkout_business_information_limpo.csv')

# Busca de cadastros do Estado de São Paulo
state_saopaulo = (len(df[df['state'] == "São Paulo" ].index))
state_sp = (len(df[df['state'] == "SP" ].index))
sp_geral = state_saopaulo + state_sp
print ('Quantidade de cadastros no estado de Sao Paulo :',sp_geral)

# Busca de cadastros do Estado da Florida

state_florida = (len(df[df['state'] == "Florida" ].index))
state_fl = (len(df[df['state'] == "FL" ].index))
fl_geral = state_florida + state_fl
print ('Quantidade de cadastros no estado da Florida :',fl_geral)

# Busca de cadastros do Estado do Rio de janeiro

state_rio_de_janeiro = (len(df[df['state'] == "Rio de Janeiro" ].index))
state_rj = (len(df[df['state'] == "RJ" ].index))
rj_geral = state_rio_de_janeiro  + state_rj
print ('Quantidade de cadastros no estado da Rio de Janeiro :',rj_geral)


# Busca de cadastros do Estado do Paraná

state_parana = (len(df[df['state'] == "Parana" ].index))
state_pr = (len(df[df['state'] == "PR" ].index))
pr_geral = state_parana  + state_pr
print ('Quantidade de cadastros no estado da Paraná :',pr_geral)

# Busca de cadastros do Estado do Goias

state_goias = (len(df[df['state'] == "Goias" ].index))
state_go = (len(df[df['state'] == "GO" ].index))
go_geral = state_goias + state_go
print ('Quantidade de cadastros no estado da Goias :',go_geral)

# Busca de cadastros do Estado do Rio grande do Sul

state_rio_grande_sul = (len(df[df['state'] == "Rio Grande do Sul" ].index))
state_rs = (len(df[df['state'] == "RS" ].index))
rs_geral = state_rio_grande_sul + state_rs
print ('Quantidade de cadastros no estado da Rio Grande do Sul :',rs_geral)


# Busca de cadastros do Estado de Minas Gerais

state_minas_gerais = (len(df[df['state'] == "Minas Gerais" ].index))
state_mg = (len(df[df['state'] == "MG" ].index))
mg_geral = state_minas_gerais + state_mg
print ('Quantidade de cadastros no estado da Minas Gerais :',mg_geral)

# Busca de cadastros do Estado do Rio grande do Norte

state_rio_grande_norte= (len(df[df['state'] == "Rio Grande do Norte" ].index))
state_rn = (len(df[df['state'] == "RN" ].index))
rn_geral = state_rio_grande_norte + state_rn
print ('Quantidade de cadastros no estado da Rio Grande do Norte :',rn_geral)

##########################################################################################################

# Busca de cadastros da Cidade de Pompeia

pompeia = (len(df[df['city'] == "Pompeia" ].index))
print ('Quantidade de cadastros da Cidade de Pompeia:',pompeia)

sao_paulo = (len(df[df['city'] == "Sao Paulo" ].index))
print ('Quantidade de cadastros da Cidade de Sao Paulo:',sao_paulo)

orlando = (len(df[df['city'] == "Orlando" ].index))
print ('Quantidade de cadastros da Cidade de Orlando:',orlando)

campinas = (len(df[df['city'] == "Campinas" ].index))
print ('Quantidade de cadastros da Cidade de Campinas:',campinas)

araraquara = (len(df[df['city'] == "Araraquara" ].index))
print ('Quantidade de cadastros da Cidade de Araraquara:',araraquara)

bauru = (len(df[df['city'] == "Bauru" ].index))
print ('Quantidade de cadastros da Cidade de Bauru:',bauru)






############################################################################################
estados = ['SP', 'FL(US)','GO', 'RJ','RS', 'PR','MG','RN']
valores_estados = [sp_geral,fl_geral,go_geral,rj_geral,rs_geral,pr_geral, mg_geral,rn_geral]

cidades = ['Sao Paulo','       \n  Pompéia','     Orlando','\n     Campinas','      Araraquara', '\n Bauru']
valores_cidades = [sao_paulo, pompeia,orlando,campinas,araraquara, bauru]

plt.figure(figsize=(10, 20))


plt.subplot(131)
plt.title('Estados')
plt.bar(estados, valores_estados)

plt.subplot(132)
plt.title('Cidades')
plt.bar(cidades, valores_cidades)

plt.suptitle('Plotagem Cadastrados')
plt.savefig('PlotagemCadastrados')
plt.show()


