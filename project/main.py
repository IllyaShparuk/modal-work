import os.path


def files_reader(file_path) -> list[str]:
    with open(file_path, "r") as file:
        content = file.readlines()
    return content


def files_writer(file_path, lines):
    with open(file_path, "w") as file:
        file.writelines(lines)


def file_сomparator(file1_lines, file2_lines):
    common_lines = list(set(file1_lines).intersection(file2_lines))

    file1_unique = [line for line in file1_lines if line not in common_lines]
    file2_unique = [line for line in file2_lines if line not in common_lines]

    return common_lines, file1_unique, file2_unique


def text_diff(file1_path, file2_path):
    file1_content_lines = files_reader(file1_path)
    file2_content_lines = files_reader(file2_path)

    common_lines, file1_unique, file2_unique = file_сomparator(file1_content_lines, file2_content_lines)

    files_writer(os.path.join("..", "results", "same.txt"), common_lines)
    files_writer(os.path.join("..", "results", "diff.txt"), file1_unique + file2_unique)


def main_module():
    file1_path = os.path.join("..", "files_to_compare", "file1.txt")
    file2_path = os.path.join("..", "files_to_compare", "file2.txt")

    text_diff(file1_path, file2_path)


if __name__ == "__main__":
    main_module()
