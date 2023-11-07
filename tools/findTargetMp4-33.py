'''筛选要展示的33个最具代表的动画，复制到目标文件夹'''

import os
import shutil

folder_path = 'smplmp4'


output_folder = os.path.join(folder_path, '33-mp4')
os.makedirs(output_folder, exist_ok=True)

file_names_to_match = [
    'BB000_003102',
    'BB000_004000',
    'BB000_006100',
    'BB000_007150',
    'BB000_007400',
    'BB000_007402',
    'BB000_020200',
    'DS3020_030010',
    'DS3020_030020',
    'DS3026_030320',
    'DS3026_030321',
    'DS3027_032060',
    'DS3028_036410',
    'DS3028_036420',
    'DS3029_030500',
    'DS3029_036240',
    'DS3030_030600',
    'DS3032_034000',
    'DS3038_034320',
    'DS3042_030321',
    'DS3051_036400',
    'ER000_005450',
    'ER000_017070',
    'ER000_060170',
    'ER000_080500',
    'ER000_080600',
    'ER000_080700',
    'ER000_080800',
    'SKR071_402000',
    'SKR073_400010',
    'SKR102_316210',
    'SKR103_316000',
    'SKR106_316110'
]

# file_names_to_match = [
#     'BB_000_003102',
#     'BB_000_004000',
#     'BB_000_006100',
#     'BB_000_007150',
#     'BB_000_007400',
#     'BB_000_007402',
#     'BB_000_020200',
#     'DS3_020_030010',
#     'DS3_020_030020',
#     'DS3_026_030320',
#     'DS3_026_030321',
#     'DS3_027_032060',
#     'DS3_028_036410',
#     'DS3_028_036420',
#     'DS3_029_030500',
#     'DS3_029_036240',
#     'DS3_030_030600',
#     'DS3_032_034000',
#     'DS3_038_034320',
#     'DS3_042_030321',
#     'DS3_051_036400',
#     'ER_000_005450',
#     'ER_000_017070',
#     'ER_000_060170',
#     'ER_000_080500',
#     'ER_000_080600',
#     'ER_000_080700',
#     'ER_000_080800',
#     'SKR_071_402000',
#     'SKR_073_400010',
#     'SKR_102_316210',
#     'SKR_103_316000',
#     'SKR_106_316110'
# ]


for root, _, files in os.walk(folder_path):
    for file in files:
        if any(file_name in file for file_name in file_names_to_match):
            source_file = os.path.join(root, file)
            target_file = os.path.join(output_folder, file)
            if source_file != target_file:
                shutil.copy2(source_file, target_file)

