import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

font_path = 'C:/WINDOWS/Fonts/BMHANNAPro.ttf' #폰트 경로
text = open('jangsongs.txt', 'r') #텍스트파일 장범준 노래 가사 몇개
result = text.read()

for number in range(0,10):
    result += result #글자 불리기

mask = np.array(Image.open('cherryblossom.png')) #이미지 마스킹
wc = WordCloud(font_path = font_path, background_color='white', mask = mask)
wc.generate(result)

f = plt.figure(figsize=(50,50))
plt.axis("off")
plt.imshow(wc)
plt.show()

f.savefig('mycloud.png')
