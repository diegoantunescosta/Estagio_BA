import pandas as pd
import matplotlib.pyplot as plt

#Buscando arquivo
dados = pd.read_csv('checkout_business_information_limpo.csv')

option = int (input("Opcao desejada: "))
cidades = []
valores_cidades = []
estados = []
valores_estados = []
if (option == 2):

    comparacoes= int (input('Quantas comparacoes deseja fazer: '))
    

    contador = 0
    while (contador < comparacoes):
        nome_cidade = str (input ('Digite o nome da Cidade: '))

        city_name= (len(dados[dados['city'] == nome_cidade].index))
   
        cidades.append(nome_cidade)
    
        valores_cidades.append(city_name)

        contador += 1
    plt.subplot(132)
    plt.title('Cidades')
    plt.bar(cidades, valores_cidades)
    plt.savefig('PlotagemCidades')
    
    
    print('Plotagem processada')

elif(option == 1):
    comparacoes= int (input('Quantas comparacoes deseja fazer: '))
    contador = 0
    while (contador < comparacoes):
        nome_estado = str (input ('Digite o nome do estado: '))

        state_name= (len(dados[dados['state'] == nome_estado].index))
   
        estados.append(nome_estado)
    
        valores_estados.append(state_name)

        contador += 1   
    
    plt.subplot(132)
    plt.title('Estados')
    plt.bar(estados, valores_estados)
    plt.savefig('PlotagemEstados')    

    print('Plotagem processada')

plt.show()    
