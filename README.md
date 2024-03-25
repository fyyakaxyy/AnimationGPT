# AnimationGPT

AnimationGPT is a project focused on generating combat style character animations based on text. This project is trained on the [MotionGPT](https://github.com/OpenMotionLab/MotionGPT) model and has produced the first character animation dataset dedicated to combat styles, named CombatMotion, which comes with textual descriptions.

**Compare to current text-to-motion dataset**

| Dataset                                                      | Motions    | Texts      | Style      | Source               |
| ------------------------------------------------------------ | ---------- | ---------- | ---------- | -------------------- |
| [KIT-ML](https://motion-annotation.humanoids.kit.edu/dataset/) | 3,911      | 6,278      | Daily      | Motion Capture       |
| [HumanML3D](https://github.com/EricGuo5513/HumanML3D)        | 14,616     | 44,970     | Daily      | Motion Capture       |
| [Motion-X](https://github.com/IDEA-Research/Motion-X)        | 81,084     | 95,642     | Daily      | Video Reconstruction |
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

Download: [google driver]()

CombatMotionProcessed(CMP) is a refined dataset that, in terms of character animation, retains 8,700 high-quality animations with a strong fighting style. In terms of textual annotations, we provide three text annotations for each animation: a concise description, a concise description with sensory details, and a detailed description.

Taking `CMP008388` as an example, its corresponding text annotations are:

```
weapon attack a man holding a Katana,executing a Charged Heavy Attack,Dual Wielding,root motion get Forward, Steady,Powerful and Relative Slow,First slow then fast,Cleanly.
weapon attack a man holding a Katana,executing a Charged Heavy Attack,Dual Wielding,root motion get Forward, Steady,Powerful and Relative Slow,First slow then fast,Cleanly,which make a sense of Piercing,Wide Open,Charged,Accumulating strength.
The character grips the wedge with both hands and charges for a powerful strike. They firmly lower their body, twist to the left, lunge forward with a bow step, and stab with the sword held in both hands.
```



### CombatMotionRaw Dataset(CMR)

Download: [google driver]()

CombatMotionRaw (CMR) is an unrefined dataset containing 14,883 animation entries (CMP is a subset of CMR), but each animation is only provided with one textual annotation. Moreover, the textual annotations in CMR consist of simple concatenations of annotated words. It was found during project development that models trained with this type of annotation performed poorly, thus this format was ultimately not adopted.

Example of textual annotation:

```
weapon attack curved sword curved greatsword right-handed one-handed charged heavy attack forward steady powerful charged accumulating strength cleanly first slow then fast slash smooth and coherent wide open featherlike roundabout lean over and twist your waist to the left step forward with your right leg store your right hand from the left back swing it diagonally downward and swing two circles.
```

CMR has a richer set of animation data, unfortunately, the annotations are not detailed enough. You can read the textual annotations from the dataset yourself and refine them.

## Model and Evaluation

Here are models trained on the CMP dataset using different algorithms:

- MotionGPT：[google driver]()
- MLD：[google driver]()
- MDM：[google driver]()

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

## Some Suggestions

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
