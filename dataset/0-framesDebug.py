'''筛选new_joint_vecs和new_joints中帧数错误的文件，移动到error文件夹中'''

import os
import shutil
import numpy as np

def find_and_copy_mismatched_files(src_folder1, src_folder2, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    dest_subfolder1 = os.path.join(dest_folder, 'old', 'new_joint_vecs')
    dest_subfolder2 = os.path.join(dest_folder, 'old', 'new_joints')

    if not os.path.exists(dest_subfolder1):
        os.makedirs(dest_subfolder1)
    if not os.path.exists(dest_subfolder2):
        os.makedirs(dest_subfolder2)

    for root, dirs, files in os.walk(src_folder1):
        for file in files:
            file_path1 = os.path.join(root, file)
            file_path2 = os.path.join(src_folder2, file)

            if os.path.exists(file_path2):
                arr1 = np.load(file_path1)
                arr2 = np.load(file_path2)

                if arr1.shape[0] != arr2.shape[0]:
                    dest_path1 = os.path.join(dest_subfolder1, file)
                    dest_path2 = os.path.join(dest_subfolder2, file)

                    shutil.copy2(file_path1, dest_path1)
                    shutil.copy2(file_path2, dest_path2)

find_and_copy_mismatched_files('old\\new_joint_vecs', 'old\\new_joints', 'error')