import os

folder_path = 'webVis\static\S4-详版'

gif_files = [f for f in os.listdir(folder_path) if f.endswith('.gif')]

if not gif_files:
    print("no GIF")
else:
    with open('gifList.txt', 'w', encoding='utf-8') as txt_file:
        for gif_file in gif_files:
            img_src = f'<img src="webVis\static\S4-详版\\{gif_file}">\n'
            txt_file.write(img_src)
