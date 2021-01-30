# coding:gbk
import os
import re
import time

import requests
import datetime
# ������ȡ���°ٿ�����ͼ����µ�������ͼͼƬ
if not os.path.exists("./��ͼ��"):  # �����洴��һ���ļ������洢ͼƬ����
    os.mkdir("./��ͼ��")

url = "https://www.qiushibaike.com/imgrank/page/%d/"  # ��ȡ���š���ͼ��ҳ��https://www.qiushibaike.com/imgrank/page/9/
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

starttime = datetime.datetime.now()     # ������ȡʱ�䣬��ʼʱ���

for page_Num in range(1, 14):
    new_url = format(url % page_Num)
    # ʹ��ͨ��������ȡ
    page_text = requests.get(url=new_url, headers=headers).text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'  # ����۽���ȡ��Ҫ��ͼƬurl
    img_src_list = re.findall(ex, page_text, re.S)
    for src in img_src_list:
        src = "https:" + src
        img_data = requests.get(url=src, headers=headers).content
        img_name = src.split("/")[-1]  # ��ͼƬ��ַ�����һ����ΪͼƬ���ƣ��ԡ�/�����б���Ƭ��
        img_path = "./��ͼ��/" + img_name
        with open(img_path, "wb") as fp:
            fp.write(img_data)
            print(img_name, "��ȡ��һ��ͼƬ����")
print("All ready!!--->>��ȡʱ�䣺", time.asctime(time.localtime(time.time())))
endtime = datetime.datetime.now()       # ������ȡʱ�䣬����ʱ���
print("��ȡ��ʱ(��)��", (endtime - starttime).seconds)
