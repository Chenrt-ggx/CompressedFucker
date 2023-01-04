import zipfile
from lib.lib_exception import CompressedFileNotExist, WrongZipFileFormat


def file_check(file: str) -> None:
    try:
        with open(file, 'r') as _:
            file = zipfile.ZipFile(file)
            file.close()
    except FileNotFoundError:
        raise CompressedFileNotExist
    except zipfile.BadZipfile:
        raise WrongZipFileFormat


def test_unzip(file: str, pwd: str = None) -> bool:
    import pyzipper as lib
    try:
        with lib.AESZipFile(file) as w_file:
            w_file.setpassword(pwd.encode())
            w_file.testzip()
        return True
    except RuntimeError as exception:
        if 'Bad password' in str(exception):
            return False
        raise exception
