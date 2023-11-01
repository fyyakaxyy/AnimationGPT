import pandas as pd
import os

excel_path = "soul_v3采样_759.xlsx"
df = pd.read_excel(excel_path)

id_to_name = dict(zip(df['ID'], df['Npy']))

npy_folder = "npy"
for filename in os.listdir(npy_folder):
    # get number  --> number_out.npy
    file_id = int(filename.split('_')[0])
    # check ID
    if file_id in id_to_name:
        new_filename = id_to_name[file_id] + "_mGPT.npy"
        os.rename(os.path.join(npy_folder, filename), os.path.join(npy_folder, new_filename))

print("Files renamed successfully!")