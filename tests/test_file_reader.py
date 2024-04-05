import pytest
from project.main import files_reader


@pytest.mark.usefixtures("real_data_fixture")
def test_file_reader(real_data_fixture):
    file1, file2 = real_data_fixture

    file1_content = ["1\n",
                     "2\n",
                     "3\n"]
    file2_content = ["1\n",
                     "2\n"]

    assert files_reader(file1) == file1_content
    assert files_reader(file2) == file2_content
