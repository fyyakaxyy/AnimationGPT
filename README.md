



# animationGPT

[webpage](https://fyyakaxyy.github.io/animationGPT/)

Character animation generation based on text-to-motion and large models

## Dataset

数据集制作和其他问题：[dataset.md](./dataset/dataset.md)

| Version      | Size                  | Notes                                                        |
| ------------ | --------------------- | ------------------------------------------------------------ |
| soul_v1(old) | 30140<br />(-M=15070) | 1. 删除了镜像npy（mirror）后文件数是15070；<br />2. 注意：Mean.npy和Std.npy的计算不包括镜像文件；<br />3. 部分动画new_joints缺失帧数信息，导致对应的new_joint_vecs的帧数为1。 |
| soul_v2      | 14993                 | 1. shinnobi和grappling缺失词性标注导致模型训练崩溃。         |
| soul_v3      | 11555                 | 1. 部分标注异常，例如“The character performs the '忍义手' pose ”；<br />2. 多个标注内容重复（GPT标注问题）：<br />其中5个重复（12）、4个重复（19）、3个重复（153）、2个重复（863）。 |
| soul_v4      | 8714                  | 1. 两版标注（一简、二简；对应的soul_v3是详细版表述）；<br />2. 侧重对root motion的方位词描述；<br />3. 增加了帧数的描述。 |



## Experiment

**evaluation on mGPT**

| Metric                                   | soul_v3           | HSmerge           | Finetune-H+S3 | soul_v4           |
| ---------------------------------------- | ----------------- | ----------------- | ------------- | ----------------- |
| Matching Score↓                          | 6.1470±0.0140     | **6.1315±0.0182** | 6.1942±0.0127 | 6.2765±0.0183     |
| Matching Score (vald)↓ (gt for MLD/mGPT) | 5.5185±0.0043     | **3.5719±0.0056** | 5.5185±0.0043 | 5.8100±0.0042     |
| R_precision (top 1)↑                     | 0.0668±0.0018     | **0.1825±0.0028** | 0.0364±0.0018 | 0.0342±0.0012     |
| R_precision (top 2)↑                     | 0.1250±0.0031     | **0.2781±0.0034** | 0.0697±0.0029 | 0.0673±0.0015     |
| R_precision (top 3)↑                     | 0.1730±0.0031     | **0.3452±0.0033** | 0.1043±0.0037 | 0.0980±0.0015     |
| R_precision (gt top 1)↑                  | 0.0929±0.0019     | **0.4466±0.0031** | 0.0929±0.0019 | 0.0312±0.0011     |
| R_precision (gt top 2)↑                  | 0.1586±0.0023     | **0.5879±0.0024** | 0.1586±0.0023 | 0.0650±0.0011     |
| R_precision (gt top 3)↑                  | 0.2130±0.0029     | **0.6612±0.0020** | 0.2130±0.0029 | 0.0966±0.0014     |
| FID↓                                     | 1.3792±0.0498     | 0.9084±0.0255     | 1.9095±0.0342 | **0.4270±0.0215** |
| Diversity→                               | **5.7904±0.0510** | 8.3893±0.0752     | 4.6923±0.0325 | 5.0881±0.0410     |
| Diversity (vald)→ (gt for  MLD/mGPT)     | **5.6903±0.0740** | 8.5648±0.0603     | 5.6903±0.0740 | 5.1668±0.0650     |
| MultiModality ↑                          | 3.6207±0.0872     | **5.8888±0.1620** | 2.9249±0.0914 | 1.8734±0.0851     |

- 混合训练在数据量上占优势，因此刷点效果不错;
- 微调的效果最差，从网页展示的对比效果来看，数据分布被严重影响;
- soul_v4生成结果的动作风格最好，但偏离了文本描述，而且关于帧数的验证失败了；





## Acknowledgments

- Dataset: Thanks to [HumanML3D](https://github.com/EricGuo5513/HumanML3D) and [Motion-X](https://github.com/IDEA-Research/Motion-X).

- algorithm: Thanks to [MLD](https://github.com/ChenFengYe/motion-latent-diffusion), [MotionGPT](https://github.com/OpenMotionLab/MotionGPT) and [MDM](https://github.com/GuyTevet/motion-diffusion-model).

Our code is partially borrowing from them.

![感谢大佬们的项目](README.assets/感谢大佬们的项目.gif)
