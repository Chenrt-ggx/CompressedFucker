import os
import time
import datetime
import threading
from lib.lib_exception import UnsupportedFileType
from lib.test_unzip import file_check as zip_file_check, test_unzip
from lib.test_unrar import file_check as rar_file_check, test_unrar


def timestamp_print(text: str) -> None:
    print(str(datetime.datetime.now()).split('.')[0], text, sep=': ')


def get_pwd(file: str, pwd_list: list, threads: int = 1 << 5) -> str:
    method = None
    mutex = {
        'index': 0,
        'result': '',
        'lock': threading.Lock()
    }

    def test() -> None:
        while mutex['result'] == '':
            mutex['lock'].acquire()
            item = mutex['index']
            if item >= len(pwd_list):
                break
            if item > 0 and item % (1 << 9) == 0:
                timestamp_print(str(item) + ' pwd checked')
            mutex['index'] += 1
            mutex['lock'].release()
            pwd = pwd_list[item]
            if method(file, pwd):
                mutex['result'] = pwd

    if 'temp' not in os.listdir():
        os.mkdir('./temp')

    if file.lower().endswith('.zip'):
        zip_file_check(file)
        method = test_unzip
    elif file.lower().endswith('.rar'):
        rar_file_check(file)
        method = test_unrar
    else:
        raise UnsupportedFileType

    thread_list = [threading.Thread(target=test, args=()) for _ in range(min(threads, len(pwd_list)))]
    timestamp_print(str(len(thread_list)) + ' threads created')
    for i in thread_list:
        i.start()
    timestamp_print(str(len(thread_list)) + ' threads started')
    for i in thread_list:
        i.join()

    time.sleep(0.1)
    os.system('rm -rf ./temp')
    return mutex['result']
