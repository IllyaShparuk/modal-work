import os.path

import pytest
from project.main import files_writer


@pytest.fixture
def real_data_fixture():
    test_path1 = os.path.join("..", "files_to_compare", "test_file1.txt")
    test_path2 = os.path.join("..", "files_to_compare", "test_file2.txt")

    lines1 = [
        "First line"
        "Second line"
        "Third line"
    ]
    lines2 = [
        "First line"
        "123"
        "Third Line"
        "Second line"
    ]

    files_writer(test_path1, lines1)
    files_writer(test_path2, lines2)