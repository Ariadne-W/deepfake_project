# TMPDIR=~/tmp python facefusion.py headless-run \
#     -s /home/zywang/DeepfakesAdvTrack-Spring2025/generation/src/id1.png \
#     -t /home/zywang/DeepfakesAdvTrack-Spring2025/generation/dst/id0_0000_00000.png \
#     -o /home/zywang/DeepfakesAdvTrack-Spring2025/generation/merged/id0_id1_0000_00000.png

#!/bin/bash

# 定义处理单行的函数
process_line() {
    line="$1"
    line=$(echo "$line" | tr -d '[:space:]')  # 去除空格

    if [[ -z "$line" ]]; then
        return  # 跳过空行
    fi

    # 解析文件名
    IFS='_' read -r -a parts <<< "$line"
    if [[ ${#parts[@]} -lt 4 ]]; then
        echo "Invalid filename format: $line"
        return
    fi

    id0=${parts[0]}          # id0
    id1=${parts[1]}          # id1
    video_id=${parts[2]}     # 视频ID
    frame_part=${parts[3]}   # 帧号部分（如00000.png）
    frame_number=${frame_part%.png}  # 去除.png后缀

    # 构造路径
    src_path="/home/zywang/DeepfakesAdvTrack-Spring2025/generation/src/${id1}.png"
    dst_path="/home/zywang/DeepfakesAdvTrack-Spring2025/generation/dst/${id0}_${video_id}_${frame_number}.png"
    output_path="/home/zywang/DeepfakesAdvTrack-Spring2025/generation/merged/${line}"

    #执行命令
    TMPDIR=~/tmp python facefusion.py headless-run \
        -s "$src_path" \
        -t "$dst_path" \
        -o "$output_path"
}

# 导出函数以便 parallel 使用
export -f process_line

# 使用 parallel 并行执行，设置最大并发任务数（例如：4）
parallel --jobs 1 process_line :::: /home/zywang/DeepfakesAdvTrack-Spring2025/generation/image_list_unhandled.txt