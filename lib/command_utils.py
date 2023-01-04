import sys


def match_and_call(info: dict) -> bool:
    params = []
    if len(sys.argv) == len(info['pattern']) + 1:
        try:
            for i in range(len(info['pattern'])):
                if type(info['pattern'][i]) == str:
                    if info['pattern'][i] != sys.argv[i + 1]:
                        return False
                else:
                    params.append(info['pattern'][i](sys.argv[i + 1]))
        except ValueError:
            return False
        result = info['method'](*params)
        if result is not None:
            print(str(result))
        return True
    return False


def dispatch(pattern: dict) -> None:
    for i in pattern:
        if match_and_call(pattern[i]):
            return
    print('command list:')
    for i in pattern:
        print('\t' + i + ': ' + pattern[i]['text'])
