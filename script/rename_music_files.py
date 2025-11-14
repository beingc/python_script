import os
import re

def rename_music_files(directory):
    # 遍历指定目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否以.mp3结尾
        if filename.endswith('.mp3'):
            # 使用正则表达式匹配文件名
            match = re.match(r'^(.*) - (.*)\.mp3$', filename)
            if match:
                song_name = match.group(1).strip()
                artist_name = match.group(2).strip()
                # 构建新的文件名，保留.mp3后缀
                new_filename = f"{artist_name} - {song_name}.mp3"
                # 获取完整的文件路径
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)

                # 重命名文件
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: "{filename}" to "{new_filename}"')

# 使用示例：将"D:\Music\temp"替换为实际的目录路径
directory_path = r'D:\Music\temp'  # 请修改为你的音乐文件夹路径
rename_music_files(directory_path)
