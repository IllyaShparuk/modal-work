def files_reader(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content


def files_writer(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)