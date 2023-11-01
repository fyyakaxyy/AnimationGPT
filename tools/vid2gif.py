"""
把mp4文件转换为gif文件
"""

from moviepy.editor import VideoFileClip
import os

input_folder = 'mp4'
output_folder = 'gif'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_width = 256
output_height = 256

mp4_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

for mp4_file in mp4_files:
    mp4_path = os.path.join(input_folder, mp4_file)
    gif_file = os.path.splitext(mp4_file)[0] + '.gif'
    gif_path = os.path.join(output_folder, gif_file)

    # 使用VideoFileClip加载MP4文件
    video_clip = VideoFileClip(mp4_path)
    video_clip.resize((output_width, output_height)).write_gif(gif_path)

print("--------------------------------------------Finish--------------------------------------------")