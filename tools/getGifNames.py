import os

folder_path = 'webVis\static\soul_v3'

gif_files = [f for f in os.listdir(folder_path) if f.endswith('.gif')]

if not gif_files:
    print("no GIF")
else:
    with open('gifList.txt', 'w') as txt_file:
        for gif_file in gif_files:
            img_src = f'<img src="webVis\static\soul_v3\\{gif_file}">\n'
            txt_file.write(img_src)
