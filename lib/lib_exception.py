class CompressedFileNotExist(Exception):
    pass


class WrongZipFileFormat(Exception):
    pass


class WrongRarFileFormat(Exception):
    pass


class UnsupportedFileType(Exception):
    pass


class BadGenerateLengthRange(Exception):
    pass


class TooMuchGenerateResult(Exception):
    pass
