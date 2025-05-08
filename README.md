# 文件说明
## generation
generation_dst.py：从视频中批量抽取需被替换的目标帧图片

generation_src.py：从视频中批量抽取所需使用的源人脸图片

extract_frame_manul.sh：手动选取源人脸图片以替换批量抽取的得到的质量不高的源人脸图片

face.sh：使用之前抽取得到的目标帧图片与源人脸图片以进行人脸替换

find_unhandled.sh：检查image_list.txt中还有哪些图片没有生成，将这些图片名放入image_list_unhandled.txt内，以供face.sh重新生成
