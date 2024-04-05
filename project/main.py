def files_reader(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content


def files_writer(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)


def file_сomparator(file1_lines, file2_lines):
    common_lines = list(set(file1_lines).intersection(file2_lines))

    file1_unique = [line for line in file1_lines if line not in common_lines]
    file2_unique = [line for line in file2_lines if line not in common_lines]

    return common_lines, file1_unique, file2_unique
