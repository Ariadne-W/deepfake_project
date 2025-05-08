import subprocess

def extract_frames(input_list_file):
    with open(input_list_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # 跳过空行
            
            # 解析文件名
            parts = line.split('_')
            if len(parts) < 4:
                print(f"Invalid filename format: {line}")
                continue
            
            # 构建视频文件名（id0_0007.mp4）
            video_id = f"{parts[0]}_{parts[2]}"
            video_file = "/data1/zywang/Celeb-DF-v2/Celeb-real/"+f"{video_id}.mp4"
            
            # 解析帧号字符串和整数值
            frame_part = parts[3].replace('.png', '')  # 获取原始帧号字符串（如 "00060"）
            try:
                frame_number = int(frame_part)  # 转换为整数用于计算帧索引
            except ValueError:
                print(f"Invalid frame number in {line}")
                continue
            
            # 构造输出文件名（id0_0007_00060.png）
            output_file = "/home/zywang/DeepfakesAdvTrack-Spring2025/generation/dst/"+f"{parts[0]}_{parts[2]}_{frame_part}.png"
            
            # 计算FFmpeg的n参数（0-based）
            n = frame_number   # 假设帧号是1-based
            
            # 构造FFmpeg命令
            command = (
                f'ffmpeg -i "{video_file}" '
                f'-vf "select=eq(n\\,{n})" '
                '-vframes 1 '
                f'"{output_file}"'
            )
            
            try:
                # 执行命令
                subprocess.run(command, shell=True, check=True)
                print(f"成功处理: {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"处理失败: {output_file} - {e}")
            except Exception as e:
                print(f"未知错误处理 {output_file}: {e}")

if __name__ == "__main__":
    extract_frames("image_list.txt")