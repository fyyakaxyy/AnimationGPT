'''
计算标注excel中的重复情况
'''
import pandas as pd

excel_file = "soul_v3标注.xlsx"
df = pd.read_excel(excel_file)

c_column = df["Desc_EN"]

# 统计重复项和数量
duplicate_count = c_column.value_counts().reset_index()
duplicate_count.columns = ["Value", "Count"]

output_excel = "duplicateCountResult.xlsx"
with pd.ExcelWriter(output_excel) as writer:
    duplicate_count.to_excel(writer, index=False)