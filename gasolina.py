#Pacotes e Bibliotecas

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Criando o arquivo CSV

%%writefile gasolina.csv
Dia,Custo
1,5.11
2,4.99
3,5.02
4,5.21
5,5.07
6,5.09
7,5.13
8,5.12
9,4.94
10,5.03

#Transformando o arquivo CSV em DataFrame

gasolina_df = pd.read_csv('gasolina.csv')

#Construindo um gráfico de linhas com base no dataframe

gasolina_grafico = sns.lineplot(data=gasolina_df, x= "Dia", y= "Custo", color='green')
gasolina_grafico.set_title('Preço médio da gasolina na cidade de São Paulo - SP em Julho de 2021')
plt.savefig('gasolina.png')
plt.show(gasolina_grafico)

