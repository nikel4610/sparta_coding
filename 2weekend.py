import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic' #폰트설정

population = pd.read_csv('D:/project/untitled1/population04.csv') #csv파일
population2 = pd.read_csv('D:/project/untitled1/population07.csv')

city = population.groupby('군구')['유동인구수'].sum().sort_values(ascending=True)
population_gangnam = population[population['군구']=='강남구']
population2_gangnam = population2[population2['군구']=='강남구']
gangnam_data = population_gangnam.groupby('일자')['유동인구수'].sum()
gangnam2_data = population2_gangnam.groupby('일자')['유동인구수'].sum()

plt.figure(figsize=(10,5))

date_list = []
for date in gangnam_data.index:
    date_list.append(str(date))
plt.plot(date_list, gangnam_data)

date_list2 = []
for date in gangnam2_data.index:
    date_list2.append(str(date))
plt.plot(date_list2, gangnam2_data)

plt.title('4월과 7월 일자별 강남 유동인구수합')
plt.xticks(rotation = 90)
plt.show()
