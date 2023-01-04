import rarfile
import platform
import subprocess
from lib.pwd_loader import fix_password
from lib.lib_exception import CompressedFileNotExist, WrongRarFileFormat


def file_check(file: str) -> None:
    try:
        with open(file, 'r') as _:
            file = rarfile.RarFile(file)
            file.close()
    except FileNotFoundError:
        raise CompressedFileNotExist
    except rarfile.NotRarFile:
        raise WrongRarFileFormat


def test_unrar(file: str, pwd: str = None) -> bool:
    def win_test(w_file: str, w_pwd: str = None) -> bool:
        from unrar import rarfile as lib
        try:
            with lib.RarFile(w_file, pwd=w_pwd) as w_file:
                w_file.extractall('./temp')
            return True
        except RuntimeError as exception:
            if 'Bad password' in str(exception):
                return False
            raise exception

    def linux_test(l_file: str, l_pwd: str = None) -> bool:
        cmd = ['rar', 't', l_file]
        if l_pwd is not None:
            cmd.append(fix_password(l_pwd))
        cmd = ' '.join(cmd)
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='gbk', shell=True)
        stdout, stderr = proc.communicate()
        return 'All OK' in stdout and len(stderr) == 0

    if 'Windows'.lower() in platform.platform().lower():
        return win_test(file, pwd)
    elif 'Linux'.lower() in platform.platform().lower():
        return linux_test(file, pwd)
    return False
