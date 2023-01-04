# 压缩文件爆破工具

![license](https://img.shields.io/github/license/Chenrt-ggx/CompressedFucker)

## 特性

- 支持 Windows 和 Linux。
- 支持普通 RAR 文件和隐藏文件名的 RAR 文件。
- 支持普通 ZIP 文件和使用传统加密的 ZIP 文件。
- 支持有特殊符号的密码。
- 支持多线程暴力破解。

## 命令行

```plain
command list:
        [file] dict: 使用 dict 中的字典爆破
        [file] digit [start length] [finish length]: 枚举数字
        [file] upper [start length] [finish length]: 枚举大写字母        
        [file] lower [start length] [finish length]: 枚举小写字母        
        [file] alpha [start length] [finish length]: 枚举大小写字母      
        [file] alnum [start length] [finish length]: 枚举数字和大小写字母
        [file] symbol [start length] [finish length]: 枚举特殊符号       
        [file] every [start length] [finish length]: 枚举可见字符        
        self test: 脚本功能测试
```

## RAR 配置

### Windows 系统

> Windows 下使用 Python 的 unrar 包解密。

需要配置环境变量 `UNRAR_LIB_PATH`，其值为 `unrar.dll` 的路径，`bin` 目录中提供了一个可用的 `unrar.dll`。

### Linux 系统

> Linux 下使用 `rar` 命令，通过命令行调用解密。

需要安装 `rar` 包，参考命令 `sudo apt install rar`、`sudo yum install rar`、`sudo pacman -S rar`。
