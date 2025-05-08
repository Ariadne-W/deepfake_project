import subprocess

def extract_frames(input_list_file):
    for i in range(59):
        # 提取视频文件名（第二个部分 + "_0000.mp4"）
        video_id_part = "id"+str(i)  # 如 "id16"
        video_file = "/data1/zywang/Celeb-DF-v2/Celeb-real/"+f"{video_id_part}_0000.mp4"
        
        # 固定帧号为第60帧（0-based索引为59）
        frame_number = 61
        n = frame_number  # FFmpeg的帧索引是0-based
        
        # 输出文件名：第二个部分 + ".png"（如 "id16.png"）
        output_file = "/home/zywang/DeepfakesAdvTrack-Spring2025/generation/src/"+f"{video_id_part}.png"
        
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