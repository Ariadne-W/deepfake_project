ffmpeg -i "/data1/zywang/Celeb-DF-v2/Celeb-real/id58_0001.mp4" -vf "select=eq(n\,10)" \
    -vframes 1 "/home/zywang/DeepfakesAdvTrack-Spring2025/generation/src/id58.png"