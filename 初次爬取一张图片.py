# coding:gbk
import os
import re

import requests

# ������ȡ���°ٿ�����ͼ����µ�������ͼͼƬ
if not os.path.exists("./��ͼ��"):  # �����洴��һ���ļ������洢ͼƬ����
    os.mkdir("./��ͼ��")

url = "https://www.qiushibaike.com/imgrank/"  # ��ȡ���š���ͼ��ҳ��
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
# ʹ��ͨ��������ȡ
page_text = requests.get(url=url, headers=headers).text
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'  # ����۽���ȡ��Ҫ������
img_src_list = re.findall(ex, page_text, re.S)
# print(img_src_list)
for src in img_src_list:
    src = "https:" + src
    img_data = requests.get(url=src, headers=headers).content
    img_name = src.split("/")[-1]  # ��ͼƬ��ַ�����һ����ΪͼƬ���ƣ��ԡ�/�����б���Ƭ��
    img_path = "./��ͼ��/" + img_name
    with open(img_path, "wb") as fp:
        fp.write(img_data)
        print(img_name, "��ȡ��һ��ͼƬ����")
