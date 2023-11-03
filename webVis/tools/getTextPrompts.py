# 在每一行前后添加<p>标签并写入输出文件

input_file_path = 'input.txt'
output_file_path = 'output.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w',encoding='utf-8') as output_file:
    for line in input_file:
        line = line.strip()
        formatted_line = f'<p>{line}</p>\n'
        output_file.write(formatted_line)
