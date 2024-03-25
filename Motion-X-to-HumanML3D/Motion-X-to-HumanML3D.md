# Motion-X-to-HumanML3D

**pipline** ：Motion-X(npy) $\rightarrow$ AMASS(npz) $\rightarrow$ HumanML3D(npy)

**Transition Matrix Testing**: Based on the results, the transition matrix `trans_matrix` is only used to adjust the overall body posture. The issue lies in the missing action features. For example, in "Ways_To_Catch_360", the human skeleton animation lacks rotational movement. The error may occur in the step from Motion-X-to-AMASS, missing some parameters.

|                               |                                                              | ![Ways_To_Catch_SMPL](./Motion-X-to-HumanML3D.assets/Ways_To_Catch_SMPL.gif) |
| :---------------------------: | ------------------------------------------------------------ | ------------------------------------------------------------ |
|           HumanML3D           | $$\left[ \begin{matrix}   1.0 & 0.0 & 0.0 \\   0.0 & 0.0 & 1.0 \\   0.0 & 1.0 & 0.0  \end{matrix}  \right]$$ | ![Ways_To_Catch_360_HML](./Motion-X-to-HumanML3D.assets/Ways_To_Catch_360_HML.gif) |
|       Standard posture        | $$\left[ \begin{matrix}   1.0 & 0.0 & 0.0 \\   0.0 & 1.0 & 0.0 \\   0.0 & 0.0 & 1.0  \end{matrix}  \right]$$ | ![Ways_To_Catch_360_Original](./Motion-X-to-HumanML3D.assets/Ways_To_Catch_360_Original.gif) |
| rotated 90° around the x-axis | $$\left[ \begin{matrix}   1.0 & 0.0 & 0.0 \\   0.0 & 0.0 & -1.0 \\   0.0 & 1.0 & 0.0  \end{matrix}  \right]$$ | ![Ways_To_Catch_360_X90](./Motion-X-to-HumanML3D.assets/Ways_To_Catch_360_X90.gif) |
| rotated 90° around the z-axis | $$\left[ \begin{matrix}   0.0 & -1.0 & 0.0 \\   1.0 & 0.0 & 0.0 \\   0.0 & 0.0 & 1.0  \end{matrix}  \right]$$ | ![Ways_To_Catch_360_Z90](./Motion-X-to-HumanML3D.assets/Ways_To_Catch_360_Z90.gif) |
|           deviation           | $$\left[ \begin{matrix}   1.0 & 0.0 & 0.0 \\   0.0 & 1.0 & 1.0 \\   0.0 & 0.0 & 1.0  \end{matrix}  \right]$$ | ![Ways_To_Catch_360_Deflection](./Motion-X-to-HumanML3D.assets/Ways_To_Catch_360_Deflection.gif) |