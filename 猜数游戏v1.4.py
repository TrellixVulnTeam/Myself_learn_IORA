# coding:gbk
"""
V1.4,��V1.3���������Ӳ¹����ֵ�ͳ��
"""

import random

a = 1  # ����Ҫ��һ��

# ͳ�Ʋ¹�������
list1 = []

# 0-20�����������
numb = random.randint(0, 20)

# ͨ��������������
guess = int(input("-->������������0-20,���²£�"))
list1.append(guess)

# ������
print("---��......����������µĶԲ���---")

while numb != guess:
    if numb < guess:
        print("-->�´��ˣ��ٸ���λ���", end="-->")
        guess = int(input("-->������������,�����²£�"))

        # �¹���������ӵ��б�
        list1.append(guess)

        # ��¼����
        a += 1
    elif numb > guess:
        print("-->��С�ˣ��ٸ���λ���", end="-->")
        guess = int(input("-->������������,�����²£�"))

        # �¹���������ӵ��б�
        list1.append(guess)

        # ��¼����
        a += 1
    else:
        # ��¼����
        a += 1


print("--��������ϲ���¶���,�ǣ�{0} ��   ͳ����µĴ�����{1} ��--".format(guess, a))
print("--��¹��������У�{0}--".format(list1))
