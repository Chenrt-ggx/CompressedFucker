from lib.pwd_loader import *
from lib.main_runner import get_pwd
from lib.self_check import self_check
from lib.command_utils import dispatch


def solve_by_dict(file: str) -> str:
    return get_pwd(file, load_from_dict())


def solve_by_digit(file: str, start_len: int, finish_len: int) -> str:
    return get_pwd(file, load_digit(start_len, finish_len))


def solve_by_upper(file: str, start_len: int, finish_len: int) -> str:
    return get_pwd(file, load_upper(start_len, finish_len))


def solve_by_lower(file: str, start_len: int, finish_len: int) -> str:
    return get_pwd(file, load_lower(start_len, finish_len))


def solve_by_alpha(file: str, start_len: int, finish_len: int) -> str:
    return get_pwd(file, load_upper_lower(start_len, finish_len))


def solve_by_alnum(file: str, start_len: int, finish_len: int) -> str:
    return get_pwd(file, load_upper_lower_digit(start_len, finish_len))


def solve_by_symbol(file: str, start_len: int, finish_len: int) -> str:
    return get_pwd(file, load_symbol(start_len, finish_len))


def solve_by_every(file: str, start_len: int, finish_len: int) -> str:
    return get_pwd(file, load_every(start_len, finish_len))


def cli() -> None:
    dispatch({
        '[file] dict': {
            'pattern': [str, 'dict'],
            'method': solve_by_dict,
            'text': '使用 dict 中的字典爆破'
        },
        '[file] digit [start length] [finish length]': {
            'pattern': [str, 'digit', int, int],
            'method': solve_by_digit,
            'text': '枚举数字'
        },
        '[file] upper [start length] [finish length]': {
            'pattern': [str, 'upper', int, int],
            'method': solve_by_upper,
            'text': '枚举大写字母'
        },
        '[file] lower [start length] [finish length]': {
            'pattern': [str, 'lower', int, int],
            'method': solve_by_lower,
            'text': '枚举小写字母'
        },
        '[file] alpha [start length] [finish length]': {
            'pattern': [str, 'alpha', int, int],
            'method': solve_by_alpha,
            'text': '枚举大小写字母'
        },
        '[file] alnum [start length] [finish length]': {
            'pattern': [str, 'alnum', int, int],
            'method': solve_by_alnum,
            'text': '枚举数字和大小写字母'
        },
        '[file] symbol [start length] [finish length]': {
            'pattern': [str, 'symbol', int, int],
            'method': solve_by_symbol,
            'text': '枚举特殊符号'
        },
        '[file] every [start length] [finish length]': {
            'pattern': [str, 'every', int, int],
            'method': solve_by_every,
            'text': '枚举可见字符'
        },
        'self test': {
            'pattern': ['self', 'test'],
            'method': self_check,
            'text': '脚本功能测试'
        }
    })


if __name__ == '__main__':
    cli()
