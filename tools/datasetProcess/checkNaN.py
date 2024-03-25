'''检测文件夹中是否存在NaN的npy文件'''
import os
import numpy as np

def checkNan(file_path):
    try:
        data = np.load(file_path)
        if np.isnan(data).any():
            return True
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return False

def traversalFolder(folder_path):
    npy_files = [f for f in os.listdir(folder_path) if f.endswith('.npy')]
    nanFiles = []

    for file in npy_files:
        file_path = os.path.join(folder_path, file)
        if checkNan(file_path):
            nanFiles.append(file)

    return nanFiles

if __name__ == "__main__":
    folder_path = "CMR\\new_joints"
    nanFiles = traversalFolder(folder_path)

    if nanFiles:
        print("NaN files:")
        for file in nanFiles:
            print(file)
    else:
        print("No NaN")
