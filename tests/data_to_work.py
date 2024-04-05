import os
import pytest
from project.main import files_writer


@pytest.fixture
def real_data_fixture():
    file1 = os.path.join("..", "files_to_compare", "test_file1.txt")
    file2 = os.path.join("..", "files_to_compare", "test_file2.txt")

    files_writer(file1, [
        "Line 1\n",
        "Line 2\n",
        "Line 3\n",
        "Common line\n",
        "Unique line 1\n",
    ])
    files_writer(file2, [
        "Line 1\n",
        "Line 2\n",
        "Common line\n",
        "Unique line 2\n",
        "Unique line 3\n",
    ])

    yield file1, file2

    os.remove(file1)
    os.remove(file2)