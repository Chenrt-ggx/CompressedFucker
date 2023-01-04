import pyzipper
import platform
import subprocess
from lib.pwd_loader import fix_password
from lib.lib_exception import CompressedFileNotExist, WrongZipFileFormat


def file_check(file: str) -> None:
    try:
        with open(file, 'r') as _:
            file = pyzipper.AESZipFile(file)
            file.close()
    except FileNotFoundError:
        raise CompressedFileNotExist
    except pyzipper.zipfile.BadZipFile:
        raise WrongZipFileFormat


def test_unzip(file: str, pwd: str = None) -> bool:
    def win_test(w_file: str, w_pwd: str = None) -> bool:
        try:
            with pyzipper.AESZipFile(w_file) as w_file:
                w_file.setpassword(w_pwd.encode())
                w_file.testzip()
            return True
        except RuntimeError as exception:
            if 'Bad password' in str(exception):
                return False
            raise exception

    def linux_test(l_file: str, l_pwd: str = None) -> bool:
        cmd = ['7z', 't', l_file]
        if l_pwd is not None:
            cmd.append(fix_password(l_pwd))
        cmd = ' '.join(cmd)
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='gbk', shell=True)
        stdout, stderr = proc.communicate()
        return 'Everything is Ok' in stdout and len(stderr) == 0

    if 'Windows'.lower() in platform.platform().lower():
        return win_test(file, pwd)
    elif 'Linux'.lower() in platform.platform().lower():
        return linux_test(file, pwd)
    return False
