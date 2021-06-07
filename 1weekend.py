import pandas as pd
import matplotlib.pyplot as plt

pizza = pd.read_csv('D:/sparta_data/sparta_data/sparta_data/week01/data/pizza_09.csv') #csv파일 위치
pizza_sum = pizza.groupby('요일').sum()['통화건수']
sorted_pizza_data = pizza_sum.sort_values(ascending=True)

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(8,5))
plt.bar(sorted_pizza_data.index, sorted_pizza_data)

plt.title('요일별 피자 주문 총량')
pizza_gu_data = pizza.groupby('발신지_구').sum()['통화건수'].sort_values(ascending=True)
plt.figure(figsize=(20,5))
plt.bar(pizza_gu_data.index, pizza_gu_data)

plt.title('구별 피자 주문 총량')
plt.xticks(rotation=90)
plt.show()
