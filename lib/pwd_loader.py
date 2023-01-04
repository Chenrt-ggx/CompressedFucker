import os
from lib.lib_exception import BadGenerateLengthRange, TooMuchGenerateResult

visible_char = [chr(i) for i in range(32, 127)]
digit_char = [chr(i + ord('0')) for i in range(10)]
upper_char = [chr(i + ord('A')) for i in range(26)]
lower_char = [chr(i + ord('a')) for i in range(26)]

upper_lower_char = upper_char + lower_char
upper_lower_digit_char = digit_char + upper_lower_char
symbol_char = list(filter(lambda x: x not in upper_lower_digit_char, [chr(i) for i in range(32, 127)]))


def fix_password(pwd: str) -> str:
    if '"' in pwd:
        return ''.join(['-p', '"', pwd.replace('"', '\\' + '"'), '"'])
    else:
        return ''.join(['-p', pwd])


def load_from_dict(directory: str = './dict') -> list:
    content = []
    for i in os.listdir(directory):
        if i.endswith('.txt'):
            with open(directory + '/' + i, 'r') as file:
                content += list(set(file.read().split('\n')))
    return list(set(filter(lambda x: len(x) != 0, content)))


def load_by_generate(start_len: int, finish_len: int, char_list: list) -> list:
    result = []

    def check_generate() -> None:
        if start_len < 1 or finish_len < start_len:
            raise BadGenerateLengthRange
        total = 0
        for length in range(start_len, finish_len + 1):
            total += pow(len(char_list), length)
        if total > 1 << 24:
            raise TooMuchGenerateResult

    def dfs_load(pos: int, length: int, curr: str) -> None:
        if pos == length:
            result.append(curr)
            return
        for append in char_list:
            dfs_load(pos + 1, length, curr + append)

    check_generate()
    for i in range(start_len, finish_len + 1):
        dfs_load(0, i, '')
    return result


def load_digit(start_len: int, finish_len: int) -> list:
    return load_by_generate(start_len, finish_len, digit_char)


def load_upper(start_len: int, finish_len: int) -> list:
    return load_by_generate(start_len, finish_len, upper_char)


def load_lower(start_len: int, finish_len: int) -> list:
    return load_by_generate(start_len, finish_len, lower_char)


def load_upper_lower(start_len: int, finish_len: int) -> list:
    return load_by_generate(start_len, finish_len, upper_lower_char)


def load_upper_lower_digit(start_len: int, finish_len: int) -> list:
    return load_by_generate(start_len, finish_len, upper_lower_digit_char)


def load_symbol(start_len: int, finish_len: int) -> list:
    return load_by_generate(start_len, finish_len, symbol_char)


def load_every(start_len: int, finish_len: int) -> list:
    return load_by_generate(start_len, finish_len, visible_char)
