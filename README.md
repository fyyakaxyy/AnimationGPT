



# animationGPT

Character animation generation based on text-to-motion and large models

全部实验的可视化结果见`webShow.html`，暂未部署到服务器，需要git到本地查看。

## Dataset

数据集制作和其他问题：[dataset.md](./dataset/dataset.md)

| Version      | Size                          | Notes                                                        |
| ------------ | ----------------------------- | ------------------------------------------------------------ |
| soul_v1(old) | 30368(with mirror)<br />15473 | 1. 删除了镜像npy（mirror）后文件数是15473；<br />2. 注意：Mean.npy和Std.npy的计算不包括镜像文件。 |
| soul_v2      | 14993                         | 1. shinnobi和grappling缺失词性标注导致模型训练崩溃。         |
| soul_v3      | 11662                         | 1. 部分标注异常，例如“The character performs the '忍义手' pose ”；<br />2. 多个标注内容重复（GPT标注问题）：<br />其中5个重复（12）、4个重复（19）、3个重复（153）、2个重复（863）。 |
| soul_v4      |                               | Todo                                                         |



**visualization**

| ![BB_000_007151_original](README.assets/BB_000_007151_original.gif) | ![BB_000_019560_original](README.assets/BB_000_019560_original.gif) | ![DS3_020_030321_original](README.assets/DS3_020_030321_original.gif) |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| ![DS3_020_034341_original](README.assets/DS3_020_034341_original.gif) | ![DS3_025_034020_original](README.assets/DS3_025_034020_original.gif) | ![DS3_029_032030_original](README.assets/DS3_029_032030_original.gif) |
| ![DS3_154_036230_original](README.assets/DS3_154_036230_original.gif) | ![ER_033_030605_original](README.assets/ER_033_030605_original.gif) | ![SKR_106_316300_original](README.assets/SKR_106_316300_original.gif) |



## Experiment and Animation

当前页面只展示最新结果，其它结果：[animation.md](./animation/animation.md)

### Finetune-H+S3

| ![DS3028_030320_mGPT](README.assets/DS3028_030320_mGPT.gif) | ![DS3042_030500_mGPT](README.assets/DS3042_030500_mGPT.gif) | ![DS3038_030340_mGPT](README.assets/DS3038_030340_mGPT.gif) |
| :---------------------------------------------------------: | :---------------------------------------------------------: | ----------------------------------------------------------- |

- 相较于单独训练和混合训练，微调的效果最差，语义理解错误，动作扭曲。
- 但是微调模型生成的动作序列时间更长。

**evaluation on mGPT**

| Metric                                   | soul_v3           | HSmerge           | Finetune-H+S3 |
| ---------------------------------------- | ----------------- | ----------------- | ------------- |
| Matching Score↓                          | 6.1470±0.0140     | **6.1315±0.0182** | 6.1942±0.0127 |
| Matching Score (vald)↓ (gt for MLD/mGPT) | 5.5185±0.0043     | **3.5719±0.0056** | 5.5185±0.0043 |
| R_precision (top 1)↑                     | 0.0668±0.0018     | **0.1825±0.0028** | 0.0364±0.0018 |
| R_precision (top 2)↑                     | 0.1250±0.0031     | **0.2781±0.0034** | 0.0697±0.0029 |
| R_precision (top 3)↑                     | 0.1730±0.0031     | **0.3452±0.0033** | 0.1043±0.0037 |
| R_precision (gt top 1)↑                  | 0.0929±0.0019     | **0.4466±0.0031** | 0.0929±0.0019 |
| R_precision (gt top 2)↑                  | 0.1586±0.0023     | **0.5879±0.0024** | 0.1586±0.0023 |
| R_precision (gt top 3)↑                  | 0.2130±0.0029     | **0.6612±0.0020** | 0.2130±0.0029 |
| FID↓                                     | 1.3792±0.0498     | **0.9084±0.0255** | 1.9095±0.0342 |
| Diversity→                               | **5.7904±0.0510** | 8.3893±0.0752     | 4.6923±0.0325 |
| Diversity (vald)→ (gt for  MLD/mGPT)     | **5.6903±0.0740** | 8.5648±0.0603     | 5.6903±0.0740 |
| MultiModality ↑                          | 3.6207±0.0872     | **5.8888±0.1620** | 2.9249±0.0914 |

**从评估指标来看，混合训练在数据量上占优势，因此刷点效果不错，视觉效果待评价。微调的效果最差，从网页展示的对比效果来看，数据分布被严重影响。**
