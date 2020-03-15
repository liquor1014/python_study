import jieba
from datetime import datetime
from wordcloud import WordCloud
from scipy.misc import imread


# 读取文件
with open('D:/Python/Text1/wenjian/徐霞客游记.txt', 'r', encoding='utf-8') as  f:
    text = f.read()
    #  分词
word_list = jieba.lcut(text)

img = imread('china.jpg')
excludes = {"五里", "二里", "西南", "东南", "三里", "十里", "西北", "东北", "不能","静闻", "一里", "转而", "其中", "至此", "二十里", "于是", "久之", "之上",
            "以为", "不知", "十五里", "不及", "不可", "大道", "东西", "南向", "其下",'下山','其内','北向','下午','南下','土人','半里','南北','三十里','不得',
            '其上','所谓','其间','之下','从此','而入','西行','西向','上下','ng','南行','其处','之水','宛转','之间','登山','由此','七里','山峡','两崖','出洞',
            '山顶','晨餐','东向','而后','之后','其南','中有','其西','之西','其东','其地','峰顶','不见','两旁','始知','其北','泊于','上午','其后','之中','饭于',
            '西门','山下','诸峰','石门','绝顶','小径','先是','下坠','四十里','一洞','西峰','其洞','观音','大山','而北','北门','宿于','一小','一岭','两山','一石',
            '顾仆','悬崖','穹然','直上','导者','门外','洞口','北上','其岩','北流','日记','其前','登岭','下瞰','深入'}

words = jieba.lcut(text)
counts = {}

for word in words:
    if len(word) == 1:
        continue # 排除分词为一的结果
    else:
        counts[word] = counts.get(word,0) +1
        # 给字典的键赋值
counts['泰山'] = counts.get('南门') + counts.get('泰山')

for word in excludes:
    del counts[word]

# 转化成列表排序
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
# print(items)

li = []

for i in range(17):
    word, count = items[i]
    print(word, count)

    for _ in range(count):
        li.append(word)

cloud_text =','.join(li)
# print(cloud_text)
#  collocations : bool, default=True //是否包括两个词的搭配
wc = WordCloud(background_color='white',width=800, height=600
,font_path='msyh.ttc', collocations=False, mask=img).generate(cloud_text)

wc.to_file('徐霞客游记地点词频统计.png')

data = str(datetime.now()).encode('utf-8')
print(data.decode('utf-8'))