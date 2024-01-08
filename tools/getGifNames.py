import os

folder_path = 'webVis\static\original_animation_SMPL'

gif_files = [f for f in os.listdir(folder_path) if f.endswith('.gif')]

if not gif_files:
    print("no GIF")
else:
    with open('gifList.txt', 'w', encoding='utf-8') as txt_file:
        for gif_file in gif_files:
            img_src = f'<img src="webVis\static\original_animation_SMPL\\{gif_file}">\n'
            txt_file.write(img_src)
