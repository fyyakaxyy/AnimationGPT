'''
把mp4转换成gif
默认视频文件位于mp4文件夹，转换的gif保存在gif文件夹中，缩放系数0.3

python vid2gif.py mp4_folder gif_folder --scale 0.3
'''

import argparse
from moviepy.editor import VideoFileClip
import os

def mp4_to_gif(mp4_folder, gif_folder, scale, fps=5, colors=256):
    if not os.path.exists(gif_folder):
        os.makedirs(gif_folder)

    mp4_files = [f for f in os.listdir(mp4_folder) if f.endswith('.mp4')]

    for mp4_file in mp4_files:
        mp4_path = os.path.join(mp4_folder, mp4_file)
        gif_file = os.path.splitext(mp4_file)[0] + '.gif'
        gif_path = os.path.join(gif_folder, gif_file)

        # 使用VideoFileClip加载MP4文件
        video_clip = VideoFileClip(mp4_path)

        gif_width = int(video_clip.size[0] * scale)
        gif_height = int(video_clip.size[1] * scale)

        # 降低帧率并减少色彩位数
        video_clip.resize((gif_width, gif_height)).write_gif(gif_path, fps=fps, colors=colors)

    print("--------------------------------------------Finish--------------------------------------------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert MP4 files to GIF files with adjustable output size.')
    parser.add_argument('mp4_folder', nargs='?', default="mp4", help='Folder of MP4 files')
    parser.add_argument('gif_folder', nargs='?', default="gif", help='Folder for saving GIF files')
    parser.add_argument('--scale', type=float, default=0.3, help='Scale factor for adjusting GIF size (default: 0.3)')
    parser.add_argument('--fps', type=int, default=15, help='Frames per second for GIF (default: 5)')
    parser.add_argument('--colors', type=int, default=256, help='Number of colors in GIF (default: 256)')

    args = parser.parse_args()
    
    mp4_to_gif(args.mp4_folder, args.gif_folder, args.scale, args.fps, args.colors)
