'''
python vid2gif.py input_folder output_folder --scale 0.8
'''

import argparse
from moviepy.editor import VideoFileClip
import os

def convert_mp4_to_gif(input_folder, output_folder, scale):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    mp4_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

    for mp4_file in mp4_files:
        mp4_path = os.path.join(input_folder, mp4_file)
        gif_file = os.path.splitext(mp4_file)[0] + '.gif'
        gif_path = os.path.join(output_folder, gif_file)

        # 使用VideoFileClip加载MP4文件
        video_clip = VideoFileClip(mp4_path)

        # 根据比例调整宽度和高度
        output_width = int(video_clip.size[0] * scale)
        output_height = int(video_clip.size[1] * scale)

        video_clip.resize((output_width, output_height)).write_gif(gif_path)

    print("--------------------------------------------Finish--------------------------------------------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert MP4 files to GIF files with adjustable output size.')
    parser.add_argument('input_folder', nargs='?', default="mp4", help='Input folder containing MP4 files')
    parser.add_argument('output_folder', nargs='?', default="gif", help='Output folder for saving GIF files')
    parser.add_argument('--scale', type=float, default=0.3, help='Scale factor for adjusting output size (default: 0.3)')

    args = parser.parse_args()
    
    convert_mp4_to_gif(args.input_folder, args.output_folder, args.scale)
