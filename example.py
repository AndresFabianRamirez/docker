import main
import functions
import pandas as pd

usuario=input('Continente a filtrar \n *Africa \n *Europe \n *Asia \n *North America \n *South America \n *Oceania \n')
#USANDO PANDAS
df = pd.read_csv('./WORLD.csv')
df = df [df['Continent']==usuario]
print(df)

""" diccionarioListo = main.list_diccionario('./WORLD.csv')
diccionarioListo = list(filter(lambda x: x['Continent']==usuario,diccionarioListo))
countries = list(map(lambda x: x['Country/Territory'],diccionarioListo))
print(countries)
porcentajes = list(map(lambda x: float(x['World Population Percentage']),diccionarioListo))
print(porcentajes) """

countries = df['Country/Territory'].values
porcentajes = df['World Population Percentage'].values

functions.graficaCircular(usuario,countries,porcentajes)


