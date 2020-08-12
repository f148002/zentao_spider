import os
import re


def get_ids():
    path = r"C:\Users\f1480\Documents\禅道/"  # 目标路径

    """os.listdir(path) 操作效果为 返回指定路径(path)文件夹中所有文件名"""
    filename_list = os.listdir(path)  # 扫描目标路径的文件,将文件名存入列表

    all_id = []
    for i in filename_list:
        id = re.search(r'(\d{3})', i).group(1)
        all_id.append(id)

    return all_id