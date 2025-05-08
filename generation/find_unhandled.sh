#!/bin/bash

# 定义路径
merged_dir="/home/zywang/DeepfakesAdvTrack-Spring2025/generation/merged"
input_list="image_list.txt"
output_unhandled="image_list_unhandled.txt"

# 清空或创建输出文件
> "$output_unhandled"

# 逐行读取image_list.txt并检查文件是否存在
while IFS= read -r line; do
    # 去除行首尾空格
    file=$(echo "$line" | tr -d '[:space:]')
    
    if [[ -z "$file" ]]; then
        continue  # 跳过空行
    fi

    # 构造完整路径
    full_path="$merged_dir/$file"

    # 如果文件不存在，则记录到未处理列表
    if [[ ! -f "$full_path" ]]; then
        echo "$file" >> "$output_unhandled"
    fi
done < "$input_list"

# 输出统计信息
count=$(wc -l < "$output_unhandled")
echo "未处理的文件数量：$count"
echo "结果已保存到：$output_unhandled"