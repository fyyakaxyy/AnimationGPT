'''
找出数据集中造成异常的原因：shinnobi和grappling
将相应的npy文件和txt文件移动到保存异常数据的文件夹中
'''

import os
import shutil

# 创建“shinnobi异常”文件夹或者"grappling异常"文件夹，保存异常文件
for folder_name in ["texts", "new_joint_vecs", "new_joints"]:
    exception_folder = os.path.join(folder_name, "grappling异常")
    os.makedirs(exception_folder, exist_ok=True)

txt_folder = "texts"
exception_filenames = []
for filename in os.listdir(txt_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(txt_folder, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            if "grappling" in content:
                exception_filenames.append(os.path.splitext(filename)[0])  # 记录不含后缀的文件名

# 移动异常npy文件到“shinnobi异常”文件夹（texts文件夹中的异常txt文件也会被移动）
for folder_name in ["texts", "new_joint_vecs", "new_joints"]:
    for filename in exception_filenames:
        src_path = os.path.join(folder_name, f"{filename}.npy" if folder_name != "texts" else f"{filename}.txt")
        dest_folder = os.path.join(folder_name, "grappling异常")
        os.makedirs(dest_folder, exist_ok=True)
        dest_path = os.path.join(dest_folder, f"{filename}.npy" if folder_name != "texts" else f"{filename}.txt")
        if os.path.exists(src_path):
            shutil.move(src_path, dest_path)