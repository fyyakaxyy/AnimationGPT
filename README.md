# AnimationGPT

[webpage（coming soon：网页备案中）]()

AnimationGPT is a project focused on generating combat style character animations based on text. This project is trained on the [MotionGPT](https://github.com/OpenMotionLab/MotionGPT) model and has produced the first character animation dataset dedicated to combat styles, named CombatMotion, which comes with textual descriptions.

**Compare to current text-to-motion dataset**

| Dataset                                                      | Motions    | Texts      | Style      | Source               |
| ------------------------------------------------------------ | ---------- | ---------- | ---------- | -------------------- |
| [KIT-ML](https://motion-annotation.humanoids.kit.edu/dataset/) | 3,911      | 6,278      | Daily Life | Motion Capture       |
| [HumanML3D](https://github.com/EricGuo5513/HumanML3D)        | 14,616     | 44,970     | Daily Life | Motion Capture       |
| [Motion-X](https://github.com/IDEA-Research/Motion-X)        | 81,084     | 95,642     | Daily Life | Video Reconstruction |
| **CMP**                                                      | **8700**   | **26,100** | **Combat** | **Game**             |
| **CMR**                                                      | **14,883** | **14,883** | **Combat** | **Game**             |

Compared to the current text-to-motion datasets, CombatMotion has the following characteristics:

1. Derived from game assets.
2. Features a fighting style, where the animation style in action games tends to be concentrated, and the types of actions are biased.
3. More detailed textual annotations.

## Combat Motion Dataset

###  Pipline

1. Obtain game assets in FBX format, redirect them to SMPL, and read the coordinates of human body joints (refer to [Fbx2SMPL](https://github.com/syan2018/Fbx2SMPL));

2. Add textual annotations. For each animation, manually annotate it from the following aspects: action type, weapon type, attack type, locational words, power descriptor words, speed descriptor words, and confusion descriptor words. A partial list of terms is shown below:

   | **Action  type** | **Weapon  type** | **Attack  type** | **Locative  words** | **Power**      | **Speed**     | **Fuzzy** |
   | ---------------- | ---------------- | ---------------- | ------------------- | -------------- | ------------- | --------- |
   | Idle             | Bare Hand        | Left-Handed      | In-Place            | Light-Weighted | Swift         | Piercing  |
   | Get Hit          | Sacred Seal      | Right-Handed     | Towards Left        | Steady         | Relative Fast | Slash     |
   | Death            | Fist             | One-Handed       | Towards Right       | Heavy-Weighted | Uniform Speed | Blunt     |
   | …                | …                | …                | …                   | …              | …             | …         |

   Then, use GPT-4 to combine these annotations into sentences.

3. Process the animation and annotated data into a format compatible with [HumanML3D](https://github.com/EricGuo5513/HumanML3D).

![CombatMotion](README.assets/CombatMotion.png)

### CombatMotionProcessed Dataset(CMP)

Download: [google drive](https://drive.google.com/file/d/17tldNzQ2aFqwxwoqBAs4YqyDUnnPy8We/view?usp=drive_link)

CombatMotionProcessed(CMP) is a refined dataset that, in terms of character animation, retains 8,700 high-quality animations with a strong fighting style. In terms of textual annotations, we provide three text annotations for each animation: a concise description, a concise description with sensory details, and a detailed description.

Taking `CMP008388` as an example, its corresponding text annotations are:

```
weapon attack a man holding a Katana,executing a Charged Heavy Attack,Dual Wielding,root motion get Forward, Steady,Powerful and Relative Slow,First slow then fast,Cleanly.
weapon attack a man holding a Katana,executing a Charged Heavy Attack,Dual Wielding,root motion get Forward, Steady,Powerful and Relative Slow,First slow then fast,Cleanly,which make a sense of Piercing,Wide Open,Charged,Accumulating strength.
The character grips the wedge with both hands and charges for a powerful strike. They firmly lower their body, twist to the left, lunge forward with a bow step, and stab with the sword held in both hands.
```



### CombatMotionRaw Dataset(CMR)

Download: [google drive](https://drive.google.com/file/d/148AwoovJrnh4F0q_HbU83WCWwFooLSZj/view?usp=drive_link)

CombatMotionRaw (CMR) is an unrefined dataset containing 14,883 animation entries (CMP is a subset of CMR), but each animation is only provided with one textual annotation. Moreover, the textual annotations in CMR consist of simple concatenations of annotated words. It was found during project development that models trained with this type of annotation performed poorly, thus this format was ultimately not adopted.

Example of textual annotation:

```
weapon attack curved sword curved greatsword right-handed one-handed charged heavy attack forward steady powerful charged accumulating strength cleanly first slow then fast slash smooth and coherent wide open featherlike roundabout lean over and twist your waist to the left step forward with your right leg store your right hand from the left back swing it diagonally downward and swing two circles.
```

CMR has a richer set of animation data, unfortunately, the annotations are not detailed enough. You can read the textual annotations from the dataset yourself and refine them.

## Model and Evaluation

Here are models trained on the CMP dataset using different algorithms:

- MotionGPT Model：[google drive](https://drive.google.com/file/d/1myqSqe41JpJCd0JaIu0FVPf93FI0A22L/view?usp=drive_link)
- MLD Model：[google drive](https://drive.google.com/file/d/161gtb0vZlitE6N4B2RrKETomnTPgOQmi/view?usp=drive_link)
- MDM Model：[google drive](https://drive.google.com/file/d/1Uzb2aFsQXq4Df3SBEc7cwXv8OobwDtto/view?usp=drive_link)

**Evaluation on CMP**

| Metric                              | MotionGPT      | MLD            | MDM            |
| ----------------------------------- | -------------- | -------------- | -------------- |
| Matching  Score↓                    | 5.426  ± 0.017 | 5.753  ± 0.019 | 5.179  ± 0.013 |
| Matching  Score (Ground Truth)↓     | 5.166  ± 0.012 | 5.177  ± 0.018 | 7.220  ± 0.018 |
| R_precision  (top 1)↑               | 0.044  ± 0.002 | 0.048  ± 0.002 | 0.053  ± 0.002 |
| R_precision  (top 2)↑               | 0.084  ± 0.003 | 0.089  ± 0.003 | 0.097  ± 0.003 |
| R_precision  (top 3)↑               | 0.122  ± 0.003 | 0.126  ± 0.003 | 0.136  ± 0.004 |
| R_precision  (top 1)(Ground Truth)↑ | 0.050  ± 0.002 | 0.051  ± 0.002 | 0.030  ± 0.001 |
| R_precision  (top 2)(Ground Truth)↑ | 0.094  ± 0.002 | 0.095  ± 0.003 | 0.063  ± 0.002 |
| R_precision  (top 3)(Ground Truth)↑ | 0.133  ± 0.003 | 0.134  ± 0.004 | 0.096  ± 0.002 |
| FID↓                                | 0.531  ± 0.018 | 1.240  ± 0.036 | 0.019  ± 0.001 |
| Diversity→                          | 5.143  ± 0.052 | 5.269  ± 0.044 | 5.191  ± 0.036 |
| Diversity  (Ground Truth)→          | 5.188  ± 0.070 | 5.200  ± 0.049 | 3.364  ± 0.080 |
| MultiModality  ↑                    | 1.793 ± 0.094  | 2.618 ± 0.115  | 2.463 ± 0.102  |

## Suggestions

During the process of dataset creation and model training/tuning, you might encounter some issues in aspects like textual annotations, model training, and data augmentation. Based on our experience, we offer the following suggestions:

### Model Training Crashes Due to Errors in Textual Annotations

If you process data using the HumanML3D pipeline, you might encounter the following issues, which can lead to model training crashes:

- The textual description contains Chinese characters or Chinese punctuation;
- Some words fail to be successfully annotated with part-of-speech tags;
- Certain mathematical symbols, such as the degree symbol "°", are recognized as abnormal characters.

### Exploration of Textual Annotations

- Adding descriptions of root motion direction in the annotated text can help the model learn directional words;
- Adding frame number information to the annotated text does not enable the model to learn how to control the duration (or number of frames) of generation;
- The more detailed the textual annotations and the greater the number of different annotations for the same animation, the better the performance of the model.

### Mixed Training

Mixing the HumanML3D, KIT-ML, and CMP datasets for model training can result in significant improvements in evaluation metrics. 

However, evaluation metrics and visual effects are not equivalent. For some generated results, models trained on a mixed dataset perform worse than those trained solely on the CMP dataset. This is because differences in action styles between datasets change the data distribution, thereby affecting model performance.

### Motion-X-to-HumanML3D

We have attempted to convert [Motion-X](https://github.com/IDEA-Research/Motion-X) into the HumanML3D format for pre-training models or to expand the codebook length of VQ-VAE to increase the richness and stylization of actions. However, the work on data conversion failed. The specific content and code can be viewed [here](Motion-X-to-HumanML3D/Motion-X-to-HumanML3D.md).

## Acknowledgments

- Algorithm: Thanks to [MLD](https://github.com/ChenFengYe/motion-latent-diffusion), [MotionGPT](https://github.com/OpenMotionLab/MotionGPT) and [MDM](https://github.com/GuyTevet/motion-diffusion-model).
- Dataset: Thanks to [HumanML3D](https://github.com/EricGuo5513/HumanML3D) and [Motion-X](https://github.com/IDEA-Research/Motion-X).

Our code is partially borrowing from them.

## Citation

If you find this repository useful, please consider citing it as follows:

```
@misc{CombatMotion,
  title={AnimationGPT},
  author={Yihao Liao, Yiyu Fu, Ziming Cheng, Jiangfeiyang Wang},
  year={2024},
  howpublished={\url{https://github.com/fyyakaxyy/AnimationGPT}}
}
```

# AnimationGPT（中文）

[webpage（coming soon：网页备案中）]()

AnimationGPT是一个基于文本生成格斗风格角色动画的项目。本项目基于[MotionGPT](https://github.com/OpenMotionLab/MotionGPT)训练模型，并且制作了首个专注于格斗风格、并配备文本描述的角色动画数据集CombatMotion。

**对比现有文本-动作数据集**

| 数据集                                                       | 动作数量   | 文本数量   | 风格 | 来源     |
| ------------------------------------------------------------ | ---------- | ---------- | ---- | -------- |
| [KIT-ML](https://motion-annotation.humanoids.kit.edu/dataset/) | 3,911      | 6,278      | 日常 | 动作捕捉 |
| [HumanML3D](https://github.com/EricGuo5513/HumanML3D)        | 14,616     | 44,970     | 日常 | 动作捕捉 |
| [Motion-X](https://github.com/IDEA-Research/Motion-X)        | 81,084     | 95,642     | 日常 | 视频重建 |
| **CMP**                                                      | **8700**   | **26,100** | 格斗 | 游戏     |
| **CMR**                                                      | **14,883** | **14,883** | 格斗 | 游戏     |

与现有text-to-motion数据集相比，CombatMotion具有如下特点：

1. 来源于游戏资产。
2. 具有格斗风格，动作类游戏当中的动画风格相对来说是集中的，动作类型有偏。
3. 更详细的文本标注。

## Combat Motion数据集

###  处理流程

1. 获取fbx格式的游戏资产，重定向到SMPL，并读取人体关节点坐标（[参考Fbx2SMPL](https://github.com/syan2018/Fbx2SMPL)）；

2. 添加文本标注。对于每一条动画，首先从动作类型、武器类型、攻击类型、方位词、力量感描述词、速度描述词和困惑描述词这几个方面添加人工标注，部分词表如下所示：

   | **Action  type** | **Weapon  type** | **Attack  type** | **Locative  words** | **Power**      | **Speed**     | **Fuzzy** |
   | ---------------- | ---------------- | ---------------- | ------------------- | -------------- | ------------- | --------- |
   | Idle             | Bare Hand        | Left-Handed      | In-Place            | Light-Weighted | Swift         | Piercing  |
   | Get Hit          | Sacred Seal      | Right-Handed     | Towards Left        | Steady         | Relative Fast | Slash     |
   | Death            | Fist             | One-Handed       | Towards Right       | Heavy-Weighted | Uniform Speed | Blunt     |
   | …                | …                | …                | …                   | …              | …             | …         |

   然后通过GPT-4将这些标注连接成句子。

3. 将动画和标注数据处理成[HumanML3D](https://github.com/EricGuo5513/HumanML3D)格式的数据。

![CombatMotion](README.assets/CombatMotion.png)

### CombatMotionProcessed数据集(CMP)

下载链接：[google drive](https://drive.google.com/file/d/17tldNzQ2aFqwxwoqBAs4YqyDUnnPy8We/view?usp=drive_link)

CombatMotionProcessed(CMP)是精加工的数据集，在角色动画方面，我们保留了高质量、格斗风格强的8700个动画，在文本标注方面，我们为每一条动画提供了3条文本标注，分别是精简版描述、带有感觉描述的精简版描述和详细版描述。

以`CMP008388`为例，其对应的文本标注是：

```
weapon attack a man holding a Katana,executing a Charged Heavy Attack,Dual Wielding,root motion get Forward, Steady,Powerful and Relative Slow,First slow then fast,Cleanly.
weapon attack a man holding a Katana,executing a Charged Heavy Attack,Dual Wielding,root motion get Forward, Steady,Powerful and Relative Slow,First slow then fast,Cleanly,which make a sense of Piercing,Wide Open,Charged,Accumulating strength.
The character grips the wedge with both hands and charges for a powerful strike. They firmly lower their body, twist to the left, lunge forward with a bow step, and stab with the sword held in both hands.
```



### CombatMotionRaw数据集(CMR)

下载链接：[google drive](https://drive.google.com/file/d/148AwoovJrnh4F0q_HbU83WCWwFooLSZj/view?usp=drive_link)

CombatMotionRaw(CMR)是未经过精加工的数据集，具备14,883个的动画数据（CMP是CMR的子集），但每条动画只提供一个文本标注。另外，CMR中的文本标注是标注词的简单连接，在项目研发中发现这种标注训练的模型性能较差，因此最终未采用这种格式。

文本标注示例：

```
weapon attack curved sword curved greatsword right-handed one-handed charged heavy attack forward steady powerful charged accumulating strength cleanly first slow then fast slash smooth and coherent wide open featherlike roundabout lean over and twist your waist to the left step forward with your right leg store your right hand from the left back swing it diagonally downward and swing two circles.
```

CMR具备更丰富的动画数据，可惜标注不够精细，你可以自行读取数据集中的文本标注并优化。



## 模型和评估

以下分别是在CMP数据集上用不同算法训练的模型：

- MotionGPT Model：[google drive](https://drive.google.com/file/d/1myqSqe41JpJCd0JaIu0FVPf93FI0A22L/view?usp=drive_link)
- MLD Model：[google drive](https://drive.google.com/file/d/161gtb0vZlitE6N4B2RrKETomnTPgOQmi/view?usp=drive_link)
- MDM Model：[google drive](https://drive.google.com/file/d/1Uzb2aFsQXq4Df3SBEc7cwXv8OobwDtto/view?usp=drive_link)

**CMP数据集上的评估结果**

| Metric                              | MotionGPT      | MLD            | MDM            |
| ----------------------------------- | -------------- | -------------- | -------------- |
| Matching  Score↓                    | 5.426  ± 0.017 | 5.753  ± 0.019 | 5.179  ± 0.013 |
| Matching  Score (Ground Truth)↓     | 5.166  ± 0.012 | 5.177  ± 0.018 | 7.220  ± 0.018 |
| R_precision  (top 1)↑               | 0.044  ± 0.002 | 0.048  ± 0.002 | 0.053  ± 0.002 |
| R_precision  (top 2)↑               | 0.084  ± 0.003 | 0.089  ± 0.003 | 0.097  ± 0.003 |
| R_precision  (top 3)↑               | 0.122  ± 0.003 | 0.126  ± 0.003 | 0.136  ± 0.004 |
| R_precision  (top 1)(Ground Truth)↑ | 0.050  ± 0.002 | 0.051  ± 0.002 | 0.030  ± 0.001 |
| R_precision  (top 2)(Ground Truth)↑ | 0.094  ± 0.002 | 0.095  ± 0.003 | 0.063  ± 0.002 |
| R_precision  (top 3)(Ground Truth)↑ | 0.133  ± 0.003 | 0.134  ± 0.004 | 0.096  ± 0.002 |
| FID↓                                | 0.531  ± 0.018 | 1.240  ± 0.036 | 0.019  ± 0.001 |
| Diversity→                          | 5.143  ± 0.052 | 5.269  ± 0.044 | 5.191  ± 0.036 |
| Diversity  (Ground Truth)→          | 5.188  ± 0.070 | 5.200  ± 0.049 | 3.364  ± 0.080 |
| MultiModality  ↑                    | 1.793 ± 0.094  | 2.618 ± 0.115  | 2.463 ± 0.102  |

## 建议

在数据集制作和模型训练调优的过程中，你可能会在文本标注、模型训练、数据增强等方面遇到一些问题。基于我们的经验，给出以下建议：

### 文本标注错误导致模型训练崩溃

如果采用HumanML3D的pipline处理数据，可能会遇到以下问题，它们将会导致模型训练崩溃：

- 文本描述中包含中文字符或中文标点；
- 部分词语无法成功添加词性标注;
- 部分数学符号，例如角度"°"被识别为异常字符。

### 文本标注的探索

- 在标注文本中添加对root motion的方位词描述，可以让模型学习到方位词；
- 在标注文本中添加帧数信息，并不能让模型学会控制生成时长（或帧数）；
- 文本标注越详细、同一条动画的不同标注数量越多，模型的性能越好。

### 混合训练

将HumanML3D、KIT-ML和CMP数据集混合起来训练模型，在评估指标上会带来巨大提升，但评估指标和视觉效果并不等价，对于部分生成结果，混合训练的模型表现不如单独使用CMP数据集训练的模型，这是因为不同数据集动作风格的差异改变了数据分布，进而影响了模型的性能。

### Motion-X到HumanML3D的格式转换

我们尝试过将[Motion-X](https://github.com/IDEA-Research/Motion-X)转换成HumanML3D的格式，用于预训练模型，或者扩充VQ-VAE的码本长度来增加动作的丰富性和风格化程度，但数据转换的工作失败了。具体内容和代码在[此处](Motion-X-to-HumanML3D/Motion-X-to-HumanML3D.md)查看。

## 致谢

- 算法：感谢 [MLD](https://github.com/ChenFengYe/motion-latent-diffusion)、[MotionGPT](https://github.com/OpenMotionLab/MotionGPT) 以及 [MDM](https://github.com/GuyTevet/motion-diffusion-model)。
- 数据集：感谢 [HumanML3D](https://github.com/EricGuo5513/HumanML3D) 和 [Motion-X](https://github.com/IDEA-Research/Motion-X)。

我们的代码部分借鉴了以上工作。

## 引用

如果您觉得这个仓库对您有用，请考虑引用：

```
@misc{CombatMotion,
  title={AnimationGPT},
  author={Yihao Liao, Yiyu Fu, Ziming Cheng, Jiangfeiyang Wang},
  year={2024},
  howpublished={\url{https://github.com/fyyakaxyy/AnimationGPT}}
}
```

