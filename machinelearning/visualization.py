# -*- coding: utf-8 -*-
"""visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FofPCZt7rAOgMio8qBMyTCRdmGthoe3L

# Data visualization
"""

import pandas as pd
df = pd.read_csv('/content/apartments.tsv', sep='\t',names=["Гарчиг", "Үнэ", "Байршил", "Хэмжээ", "Давхар", "Он", "Дүүрэг", "Лизинг", "Бэлэн", "Үнэмк"])

print(df.head())

avg_prices = df.groupby(['Дүүрэг', 'Бэлэн'])['Үнэмк'].mean().reset_index()
avg_prices = avg_prices.rename(columns={'Үнэмк': 'Average Price'})
print(avg_prices)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(rc={'figure.figsize':(18.7,8.27)})

sns.barplot(x='Дүүрэг', y='Average Price', hue='Бэлэн', data=avg_prices)

avg_price_for_process=avg_prices.groupby('Бэлэн')['Average Price'].mean().reset_index()
avg_price_for_process = avg_price_for_process.rename(columns={'Average Price': 'avg'})
print(avg_price_for_process)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x="Бэлэн", y="avg", data=avg_price_for_process)
plt.title("Ашиглалтанд орсон эсэхээс МКВ үнэ")
plt.xlabel("Гүйцэтгэл")
plt.ylabel("Дундаж үнэ сая төгрөгөөр (₮)")
plt.show()

yearly_df = df.groupby([ 'Он'])['Үнэмк'].mean().reset_index()
yearly_df.head()

plt.figure(figsize=(30, 6))
sns.barplot(x="Он", y="Үнэмк", data=yearly_df)
plt.title("Баригдсан он ба үнэ")
plt.xlabel("Он")
plt.ylabel("Дундаж үнэ сая төгрөгөөр (₮)")
plt.show()

heatmap_df = df.groupby(['Дүүрэг','Он'])['Үнэмк'].mean().reset_index()
sns.heatmap(heatmap_df.pivot(index='Дүүрэг', columns='Он', values='Үнэмк'),cmap='RdBu_r')
heatmap_df.head()