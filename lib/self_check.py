import os
import time
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


def standard_test() -> None:
    print('-' * 30)
    test_four_alnum('assets/rar_all_alnum_no_name.rar')
    print('-' * 30)
    test_four_alnum('assets/rar_all_alnum_normal.rar')
    print('-' * 30)
    test_dict('assets/rar_all_dict_no_name.rar')
    print('-' * 30)
    test_dict('assets/rar_all_dict_normal.rar')
    print('-' * 30)
    test_six_digit('assets/rar_all_digit_no_name.rar')
    print('-' * 30)
    test_six_digit('assets/rar_all_digit_normal.rar')
    print('-' * 30)
    test_four_alnum('assets/zip_all_alnum_legacy.zip')
    print('-' * 30)
    test_four_alnum('assets/zip_all_alnum_normal.zip')
    print('-' * 30)
    test_dict('assets/zip_all_dict_legacy.zip')
    print('-' * 30)
    test_dict('assets/zip_all_dict_normal.zip')
    print('-' * 30)
    test_six_digit('assets/zip_all_digit_legacy.zip')
    print('-' * 30)
    test_six_digit('assets/zip_all_digit_normal.zip')


def extra_test() -> None:
    print('-' * 30)
    test_single_rar_pwd('assets/rar_linux_special_name_alpha_no_name.rar', '"')
    print('-' * 30)
    test_single_rar_pwd('assets/rar_linux_special_name_alpha_normal.rar', '"')
    print('-' * 30)
    test_single_rar_pwd('assets/rar_linux_special_name_beta_no_name.rar', '\' " \'')
    print('-' * 30)
    test_single_rar_pwd('assets/rar_linux_special_name_beta_normal.rar', '\' " \'')
    print('-' * 30)
    test_single_zip_pwd('assets/zip_all_special_name_alpha_legacy.zip', '"')
    print('-' * 30)
    test_single_zip_pwd('assets/zip_all_special_name_alpha_normal.zip', '"')
    print('-' * 30)
    test_single_zip_pwd('assets/zip_all_special_name_beta_legacy.zip', '\' " \'')
    print('-' * 30)
    test_single_zip_pwd('assets/zip_all_special_name_beta_normal.zip', '\' " \'')


def self_check() -> None:
    standard_test()
    extra_test()
    time.sleep(0.1)
    os.system('rm -rf ./temp')
    print('-' * 30)
    print('self test finished')
