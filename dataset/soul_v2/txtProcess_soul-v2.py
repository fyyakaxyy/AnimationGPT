'''
处理标注有问题的txt文件
1. 双空格->单空格
2. 删除/SPACE
3. 删除第一个#0.0#0.0以后的内容
'''

import os

def process_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    content = content.replace('  ', ' ')
    content = content.replace('/SPACE', '')
    if "#0.0#0.0" in content:
        content = content.split("#0.0#0.0", 1)[0] + "#0.0#0.0"

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

folder_path = 'texts'

for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.txt'):
            file_path = os.path.join(root, file_name)
            process_txt_file(file_path)