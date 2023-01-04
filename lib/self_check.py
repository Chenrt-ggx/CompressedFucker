import platform
from lib.main_runner import get_pwd
from lib.test_unzip import test_unzip
from lib.test_unrar import test_unrar
from lib.pwd_loader import load_from_dict, load_upper_lower_digit, load_digit


def test_single_zip_pwd(file: str, pwd: str = None) -> None:
    result = test_unzip(file, pwd=pwd)
    print('Correct' if result else 'Incorrect')


def test_single_rar_pwd(file: str, pwd: str = None) -> None:
    result = test_unrar(file, pwd=pwd)
    print('Correct' if result else 'Incorrect')


def test_four_alnum(file: str) -> None:
    gen = load_upper_lower_digit(4, 4)
    result = get_pwd(file, gen)
    print(result if result != '' else 'No Match')


def test_six_digit(file: str) -> None:
    gen = load_digit(6, 6)
    result = get_pwd(file, gen)
    print(result if result != '' else 'No Match')


def test_dict(file: str) -> None:
    gen = load_from_dict()
    result = get_pwd(file, gen)
    print(result if result != '' else 'No Match')


def self_test():
    test_six_digit('assets/rar_all_alpha.rar')
    test_dict('assets/rar_all_beta.rar')
    test_six_digit('assets/zip_all_alpha.zip')
    test_single_zip_pwd('assets/zip_all_beta.zip', '"')
    test_single_zip_pwd('assets/zip_all_gamma.zip', '\' " \'')
    if 'Linux'.lower() in platform.platform().lower():
        test_single_rar_pwd('assets/rar_linux_alpha.rar', '"')
        test_single_rar_pwd('assets/rar_linux_beta.rar', '\' " \'')
        test_six_digit('assets/zip_linux_alpha.zip')
        test_single_zip_pwd('assets/zip_linux_beta.zip', '"')
        test_single_zip_pwd('assets/zip_linux_gamma.zip', '\' " \'')
