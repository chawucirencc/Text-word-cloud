#!/usr/bin/env.python
# -*- coding: utf-8 -*-
import jieba
import numpy as np
import matplotlib.pyplot as plt
import wordcloud
from PIL import Image


"""
对《大秦帝国》整篇小说500万余字进行词云创建，其中包括设置自定义词集以及设置停用词列表，对词云的形状进行自定义。
"""
def get_text(file_name, encoding, path):
    """预处理文本，将文本分词并保存到字符串当中"""
    jieba.add_word('六国分秦')   # 自定义分词词语
    jieba.add_word('孙皓晖')
    stopwords = stop_word_list(path)    # 生成停用词列表
    file = open(file_name, 'r', encoding=encoding).readlines()  # 打开文件，编码为gb8030
    word = ''           # 词云必须为字符串形式
    for line in file:
        file2 = jieba.cut(line.strip('\n\t'))
        for i in file2:
            if i not in stopwords:      # 判断词语是否在停用词列表中
                if len(i) >= 2:
                    word += str('/') + i   # 对每个切分的字符串添加分隔符
    return word

def stop_word_list(path):
    """设置停用词列表函数"""
    stopwords = []
    file = open(path, 'r', encoding='gbk').readlines()
    for line in file:
        stopwords.append(line.strip())
    return stopwords

def image_num(image_path):
    """当绘制有图片背景的词云时使用，制作一般词云可以不用，画一般词云时可对程序适当修改"""
    image = Image.open(image_path)
    graph = np.array(image)
    return graph

def draw_word_cloud(word, graph):
    """画出词云图片，保存到本地，并可视化"""
    font_path = 'C:\\Windows\\Fonts\\Deng.ttf'      # 设置字体路径
    wc = wordcloud.WordCloud(font_path=font_path, background_color='white',
                             max_words=200, mask=graph, scale=1.5, random_state=10)  # wordCloud参数设置
    wc.generate(word)
    image_color = wordcloud.ImageColorGenerator(graph)
    wc.to_file('word9.png')                              # 将生成的文件保存起来
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis('off')
    plt.show()

def main():
    """主函数"""
    file_name = 'da_qin_di_guo.txt'          # 所要分析的文本
    path = 'stopwords.txt'                   # 停用词文件
    encoding = 'gb18030'
    word = get_text(file_name, encoding, path)
    image_path = 'ellipse.jpg'               # 设置词云形状的图片文件
    graph = image_num(image_path)
    draw_word_cloud(word, graph)


main()                                       # 调用主函数
