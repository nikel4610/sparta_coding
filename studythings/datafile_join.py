import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "Malgun Gothic" #폰트

enroll = pd.read_csv('D:/project/untitled1/sparta_data/enrolleds_detail.csv')
enroll_detail = enroll.groupby('lecture_id')['user_id'].count()
lectures = pd.read_csv('D:/project/untitled1/sparta_data/lectures.csv')

lecture_count = pd.DataFrame(enroll_detail)
lecture_count = lecture_count.reset_index() #엑셀파일처럼 보이게 다시 리셋
lecture_count = lecture_count.rename(columns={'user_id':'count'}) #csv파일 칼럼이름 수정

lectures = lectures.set_index('lecture_id')
full_lecture = lecture_count.join(lectures, on='lecture_id') #기준 합치기

plt.figure(figsize=(22,5))
plt.bar(full_lecture['title'], full_lecture['count'])
plt.title('강의에 따른 수강완료 수의 합계')
plt.xticks(rotation=90)
plt.show()
