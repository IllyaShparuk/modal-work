def files_reader(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content
