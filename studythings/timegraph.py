import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

sparta_data = pd.read_csv('D:/project/untitled1/sparta_data/enrolleds_detail.csv')
format = '%Y-%m-%dT%H:%M:%S.%f' #연월일시분초ms
sparta_data['done_date_time'] = pd.to_datetime(sparta_data['done_date'], format=format) #시간을 시간데이터로 바꾸기
sparta_data['done_date_time_weekday'] = sparta_data['done_date_time'].dt.day_name() #요일 칼럼 추가

weekdata = sparta_data.groupby('done_date_time_weekday')['user_id'].count
weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdata = weekdata.agg(weeks) #weeks기준으로 합치기 
#AttributeError: 'function' object has no attribute 'agg' *에러 해결 부탁

plt.figure(figsize=(8,5))
plt.bar(weekdata.index, weekdata)
plt.title('요일별 수강 완료 수강생 수')
plt.xlabel('요일')
plt.ylabel('수강생(명)')
plt.xticks(rotation=90)
plt.show()

#시간별로 그래프
#spatrta_data['done_date_time_hour'] = sparta_data['done_date_time'].dt.hour
#hourdata = sparta_data.groupby('done_date_time_hour')['user_id'].count()
#hourdata = hourdata.sort_index()

#plt.figure(figsize=(10,5))
#plt.plot(hourdata.index, hourdata)
#plt.title... 라벨 등등

#plt.xticks(np.arange(24)) -> 0부터 23까지 숫자 쭉
#sparta_data_pivot_table = pd.pivot_table(sparta_data, values = 'user_id', aggfunc='count', index = ['done_date_time_weekday'],
# columns = ['done_date_time_hour']).agg(weeks)

#히트맵 그리기
#plt.pcolor(sparta_data_pivot_table)
#plt.xticks(np.arange(0.5,len(sparta_data_pivot_table.columns),1),sparta_data_pivot_table.columns
#plt.yticks(np.arange(0.5,len(sparta_data_pivot_table.index),1),sparta_data_pivot_table.index
