

# t2m_Prompt注意事项

批量实现text2motion，需要将prompt保存到txt文件中，但需要注意不同项目之间的区别：

MDM的单次生成和采样数量受限于batchsize

![MDM-sample](animation.assets/MDM-sample.png)

MLD需要在文本指令前加上期望的帧数

```python
with open("MLD_t2m_soul_v3.txt", "r",encoding='utf-8') as f:
    lines = f.readlines()
    newlines = []
    for line in lines:
    # 固定帧数为100
        newlines.append(str(100)+" "+line)

    with open("t2msoulv3.txt", "w") as f:
        f.writelines(newlines)
```

