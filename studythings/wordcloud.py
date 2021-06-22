import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import matplotlib.font_manager as fm

font_path = 'C:/WINDOWS/Fonts/BMHANNAPro.ttf' #폰트 경로

for number in range(1, 15):
    index = '{:02}'.format(number) #숫자 00, 01, 02.. 순으로 만들기
    filename = "Sequence_" + index + ".txt"
    text = open('D:/project/untitled1/sparta_data/' + filename, 'r', encoding='UTF-8-sig')
    text = text.read()

#텍스트파일 특수기호 제거하기
pattern = '[^\w\s]'
text = re.sub(pattern=pattern, repl='', string = text)

#워드클라우드 이미지
mask = np.array(Image.open('D:/project/untitled1/sparta_data/sparta.png')) #png이미지파일 경로
wc = WordCloud(font_path = font_path, background_color='white', mask = mask) #워드클라우드 이미지 마스킹
wc.generate(text)

f = plt.figure(figsize=(50,50))

f.add_subplot(1,2, 1) #그래프 두개 만들기 첫번쨰
plt.imshow(mask, cmap=plt.cm.gray)
plt.title('Original Stencil', size=40)
plt.axis("off")

f.add_subplot(1,2, 2) #그래프 두개 만들기 두번째
plt.imshow(wc, interpolation='bilinear')
plt.title("Sparta Cloud", size = 40)
plt.axis("off")

plt.show()
f.savefig('D:/project/untitled1/sparta_data/myWordCloud1.png') #저장경로설정
