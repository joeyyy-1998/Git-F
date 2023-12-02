"""
作者：振华
日期：2023年04月10日
"""
import sys
import os
import random

# 下面的地址写成你要转换的文件夹的地址
data_base_dir = r"H:\FJ\Explicit-Shape-Priors-main\data_split\spine_mri\pre_img"
# 建立列表，用于保存图片信息
file_list = []
# 读取文件名，写到txt文件中，这里假设叫lable.txt
write_file_name = r'./ train1.txt'
# 以只写方式打开write_file_name文件
# write_file = open(write_file_name, "w", encoding='utf-8')
write_file = open(write_file_name, "a", encoding='utf-8')
for file in os.listdir(data_base_dir):
    write_name = file
    file_list.append(write_name)
number_of_lines = len(file_list)
# 将图片信息写入txt文件中，逐行写入
print('-----', file_list, '-------')
for current_line in range(number_of_lines):
    print(file_list)
    print(current_line)
    write_file.write(file_list[current_line]+ '\n')
# 关闭文件
write_file.close()
print('写入完成！')
