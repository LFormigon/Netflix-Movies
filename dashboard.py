import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

df = pd.read_csv('C:/Users/LEOTR/OneDrive/Área de Trabalho/Netflix-Movies/netflix_titles.csv', encoding='ISO-8859-1', skiprows=0, sep=',', skipfooter=12, thousands='.', decimal=',')

sns.countplot(x='type', data=df)
plt.show()

# Agrupa por ano de lançamento e tipo (Movie ou TV Show)
df_grouped = df.groupby(['release_year', 'type']).size().reset_index(name='count')

# Ordena os anos para o gráfico ficar bonitinho
df_grouped = df_grouped.sort_values('release_year')

# Plotando com Seaborn
plt.figure(figsize=(14, 6))
sns.lineplot(data=df_grouped, x='release_year', y='count', hue='type', marker='o')

# Agrupar por ano e tipo (Movie ou TV Show)
df_grouped = df.groupby(['release_year', 'type']).size().reset_index(name='count')

# Filtrar anos entre 2000 e 2019
df_grouped = df_grouped[(df_grouped['release_year'] >= 2000) & (df_grouped['release_year'] < 2020)]

# Ordenar os dados
df_grouped = df_grouped.sort_values('release_year')

# Plotar
plt.figure(figsize=(14, 6))
sns.lineplot(data=df_grouped, x='release_year', y='count', hue='type', marker='o')

plt.title('Quantidade de Filmes e Séries por Ano (2000 a 2019)')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()