import pandas as pd
import matplotlib.pyplot as plt
#Buscando arquivo

nome_estado = str (input ('Digite o nome do estado: '))
dados = pd.read_csv('checkout_business_information_limpo.csv')


state_name= (len(dados[dados['state'] == nome_estado ].index))


nome_estado2 = str(input ('Digite o estado que deseja comparar:'))

state_name2= (len(dados[dados['state'] == nome_estado2 ].index))


resposta = str(input ('Deseja compara mais algum estado [y/n]:'))
if resposta == 'Y' or resposta == 'y':
    
    nome_estado3 = str(input ('Digite o estado que deseja comparar:'))
    state_name3= (len(dados[dados['state'] == nome_estado3 ].index))
    estados = [nome_estado and state_name,nome_estado2,nome_estado3]
    valores_estados = [state_name,state_name2, state_name3]
    print ('Exibindo resultado')
else: 
        print ('Exibindo resultado')
        estados = [nome_estado,nome_estado2]
        valores_estados = [state_name,state_name2]


plt.figure(figsize=(10, 20))


plt.subplot(131)
plt.title('Estados')
plt.bar(estados, valores_estados)
plt.suptitle('Plotagem Cadastrados')
plt.savefig('PlotagemCadastrados')
plt.show()


