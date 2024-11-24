import os


def get_directory_path(prompt_message):
    target_path = input(prompt_message)
    if not os.path.exists(target_path) or not os.path.isdir(target_path):
        print("目录不存在！请检查输入的路径是否正确。")
        return None
    return target_path


def batch_rename_files(path, index, file_name):
    if not os.path.exists(path):
        print("指定的目录不存在！")
        return

    files = os.listdir(path)
    changes = []

    for file in files:
        old_path = os.path.join(path, file)
        if os.path.isfile(old_path) and len(file) > index:
            extension = file.split('.')[-1] if '.' in file else ''
            new_file_name = file_name + file[index:] if len(file) > index else file_name
            if extension:
                new_file_name += '.' + extension
            new_path = os.path.join(path, new_file_name)
            changes.append((old_path, new_path))

    for old_path, new_path in changes:
        print(f"将 '{old_path}' 替换为 '{new_path}' ")

    confirm = input("输入 'yes' 以确认替换操作: ")
    if confirm.lower() == 'yes':
        for old_path, new_path in changes:
            os.rename(old_path, new_path)
        print("文件重命名完成。")
    else:
        print("操作已取消。")


if __name__ == '__main__':
    directory_path = get_directory_path("请输入要修改的目录的绝对路径: ")
    if directory_path is None:
        exit()
    count = int(input("请输入即将修改的文件名字段长度: "))
    name = input("请输入新的文件名前缀: ")
    batch_rename_files(directory_path, count, name)
