



# animationGPT

Character animation generation based on text-to-motion and large models



## Dataset



| Version      | Size                          | Notes                                                        |
| ------------ | ----------------------------- | ------------------------------------------------------------ |
| soul_v1(old) | 30368(with mirror)<br />15473 | 1. 删除了镜像npy（mirror）后文件数是15473；<br />2. 注意：Mean.npy和Std.npy的计算不包括镜像文件 |
| soul_v2      | 14993                         | 1. shinnobi和grappling缺失词性标注导致模型训练崩溃。         |
| soul_v3      | 11662                         | 1. 部分标注异常，例如“The character performs the '忍义手' pose ”；<br />2. 多个标注内容相同（GPT标注问题）。 |
| soul_v4      |                               | Todo                                                         |

[dataset.md](./dataset/dataset.md)

## Experiment and Animation

当前页面只展示最新结果，其它结果：[animation.md](./animation/animation.md)

### HSmerge

|                   MDM                   |                             MLD                              |                 mGPT                  |
| :-------------------------------------: | :----------------------------------------------------------: | :-----------------------------------: |
| ![sample24](README.assets/sample24.gif) | ![Example_100_batch0_56](README.assets/Example_100_batch0_56.gif) | ![352_out](README.assets/352_out.gif) |
|                  同上                   | ![Example_100_batch0_102](README.assets/Example_100_batch0_102.gif) | ![380_out](README.assets/380_out.gif) |
|                  同上                   | ![Example_100_batch0_105](README.assets/Example_100_batch0_105.gif) | ![657_out](README.assets/657_out.gif) |

- MDM训练崩溃
- MLD的foot slide问题比较明显
