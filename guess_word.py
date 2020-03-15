import jieba
from wordcloud import WordCloud
from scipy.misc import imread
# 读取文件
with open('D:/Python/Text1/wenjian/threekingdom.txt', 'r', encoding='utf-8') as  f:
    text = f.read()
    #  分词
word_list = jieba.lcut(text)
# print(word_list)
# # 将列表转化成字符串
# words = ' '.join(word_list)
# #  绘制词云
# wc = WordCloud(
#     background_color='white',
#     height=600,
#     width=800,
#     font_path='msyh.ttc'
# ).generate(words)
# wc.to_file('三国小说词云.png')
img = imread('china.jpg')
excludes = {"将军", "却说", "丞相", "二人", "不可", "荆州", "不能", "如此", "商议",
            "如何", "主公", "军士", "军马", "左右", "次日", "引兵", "大喜", "天下",
            "东吴", "于是", "今日", "不敢", "魏兵", "陛下", "都督", "人马", "不知"}
with open('D:/Python/Text1/wenjian/threekingdom.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
words = jieba.lcut(text)
counts = {}


for word in words:
    if len(word) == 1:
        continue # 排除分词为一的结果
    else:
        counts[word] = counts.get(word,0) +1
        # 给字典的键赋值   孔明 ：1
counts['孔明'] = counts.get('孔明') + counts.get('孔明曰')
counts['玄德'] = counts.get('玄德') + counts.get('玄德曰')
counts['玄德'] = counts.get('玄德') + counts.get('刘备')
counts['云长'] = counts.get('云长') + counts.get('关公')

# print(counts)
for word in excludes:
    del counts[word]

# 转化成列表排序
items = list(counts.items())
# [('正文', 1), ('第一回', 1), ('桃园', 19), ('豪杰', 22)...
items.sort(key=lambda x: x[1], reverse=True)
# print(items)
# [('曹操', 910), ('孔明', 818), ('将军', 739), ('却说', 642), ('玄德', 515),
li = []
for i in range(10):
    word, count = items[i]
    print(word, count)

    for _ in range(count):
        li.append(word)

cloud_text =','.join(li)
# print(cloud_text)
#  collocations : bool, default=True //是否包括两个词的搭配
wc = WordCloud(background_color='white',width=800, height=600
,font_path='msyh.ttc', collocations=False, mask=img).generate(cloud_text)

wc.to_file('三国演义人物词频统计.png')

