import os
import numpy as np

def check_for_nan(file_path):
    try:
        data = np.load(file_path)
        if np.isnan(data).any():
            return True
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return False

def check_folder_for_nan(folder_path):
    npy_files = [f for f in os.listdir(folder_path) if f.endswith('.npy')]
    files_with_nan = []

    for file_name in npy_files:
        file_path = os.path.join(folder_path, file_name)
        if check_for_nan(file_path):
            files_with_nan.append(file_name)

    return files_with_nan

if __name__ == "__main__":
    folder_path = "soul_v3\\new_joints"
    files_with_nan = check_folder_for_nan(folder_path)

    if files_with_nan:
        print("NaN files:")
        for file_name in files_with_nan:
            print(file_name)
    else:
        print("No NaN")
