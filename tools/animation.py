"""
npy2mp4
matplotlib==3.3.3
"""

import os
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams['animation.ffmpeg_path'] = r'D:\\T2MGPT\\ffmpeg\\bin\\ffmpeg.exe'
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import mpl_toolkits.mplot3d.axes3d as p3
from tqdm import tqdm

def plot_3d_motion(save_path, kinematic_tree, joints, title, figsize=(10, 10), fps=120, radius=4):
    def init(fig, ax):
        ax.set_xlim3d([-radius / 2, radius / 2])
        ax.set_ylim3d([0, radius])
        ax.set_zlim3d([0, radius])
        fig.suptitle(title, fontsize=20)
        ax.grid(b=False)

    def plot_xz_plane(minx, maxx, miny, minz, maxz):
        verts = [
            [minx, miny, minz],
            [minx, miny, maxz],
            [maxx, miny, maxz],
            [maxx, miny, minz]
        ]
        xz_plane = Poly3DCollection([verts], alpha=0.5)
        xz_plane.set_facecolor((0.5, 0.5, 0.5))
        ax.add_collection3d(xz_plane)

    data = joints.copy().reshape(len(joints), -1, 3)  # (seq_len, joints_num, 3)
    fig = plt.figure(figsize=figsize)
    ax = p3.Axes3D(fig)
    init(fig, ax)
    MINS = data.min(axis=0).min(axis=0)
    MAXS = data.max(axis=0).max(axis=0)
    colors = ['red', 'blue', 'black', 'red', 'blue',
              'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue',
              'darkred', 'darkred', 'darkred', 'darkred', 'darkred']
    frame_number = data.shape[0]

    height_offset = MINS[1]
    data[:, :, 1] -= height_offset
    trajec = data[:, 0, [0, 2]]

    data[..., 0] -= data[:, 0:1, 0]
    data[..., 2] -= data[:, 0:1, 2]

    def update(index):
        ax.lines = []
        ax.collections = []

        ax.view_init(elev=120, azim=-90)
        ax.dist = 7.5
        plot_xz_plane(MINS[0] - trajec[index, 0], MAXS[0] - trajec[index, 0], 0, MINS[2] - trajec[index, 1],
                      MAXS[2] - trajec[index, 1])

        if index > 1:
            ax.plot3D(trajec[:index, 0] - trajec[index, 0], np.zeros_like(trajec[:index, 0]),
                       trajec[:index, 1] - trajec[index, 1], linewidth=1.0,
                       color='blue')

        for i, (chain, color) in enumerate(zip(kinematic_tree, colors)):
            linewidth = 4.0 if i < 5 else 2.0
            ax.plot3D(data[index, chain, 0], data[index, chain, 1], data[index, chain, 2], linewidth=linewidth,
                       color=color)

        plt.axis('off')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])

    ani = FuncAnimation(fig, update, frames=frame_number, interval=1000 / fps, repeat=False)

    ani.save(save_path, fps=fps)
    plt.close()

def npy2mp4(npy_folder, mp4_folder, kinematic_chain):
    npy_files = [os.path.join(root, file)
                 for root, dirs, files in os.walk(npy_folder)
                 for file in files if file.endswith(".npy")]

    for npy_file in tqdm(npy_files):
        data = np.load(npy_file, allow_pickle=True).reshape(-1, 22, 3)

        assert data.shape[-2:] == (22, 3), f"Unexpected data shape for file: {npy_file}"

        relative_path = os.path.relpath(npy_file, npy_folder)
        npy_filename = os.path.splitext(os.path.basename(npy_file))[0]
        save_path = os.path.join(mp4_folder, f"{npy_filename}.mp4")
        save_dir = os.path.dirname(save_path)

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        if os.path.exists(save_path):
            continue
        # plot_3d_motion(save_path, kinematic_chain, data, title=npy_filename, fps=30, radius=4)
        plot_3d_motion(save_path, kinematic_chain, data, title=None, fps=30, radius=4)

if __name__ == "__main__":
    npy_folder = 'npy'
    mp4_folder = os.path.join(npy_folder, "animation")
    kinematic_chain = [[0, 2, 5, 8, 11], [0, 1, 4, 7, 10], [0, 3, 6, 9, 12, 15], [9, 14, 17, 19, 21], [9, 13, 16, 18, 20]]
    os.makedirs(mp4_folder, exist_ok=True)

    npy2mp4(npy_folder, mp4_folder, kinematic_chain)