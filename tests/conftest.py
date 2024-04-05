import os
import pytest
from project.main import files_writer


@pytest.fixture
def real_data_fixture():
    file1 = os.path.join("test_file1.txt")
    file2 = os.path.join("test_file2.txt")

    files_writer(file1, [
        "1\n",
        "2\n",
        "3\n"
    ])
    files_writer(file2, [
        "1\n",
        "2\n"
    ])

    yield file1, file2

    os.remove(file1)
    os.remove(file2)