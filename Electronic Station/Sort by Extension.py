from typing import List
from itertools import groupby
import re


def sort_by_ext(files: List[str]) -> List[str]:

    temp_exts = []
    names = []
    for item in files:
        if re.match('^.+\..+$', item) and not item.endswith('.'):
            temp_exts.append(item)
        else:
            names.append(item)

    names.sort()
    temp_exts.sort(key=lambda ext: re.search('^(.+)\.(.+)$', ext).group(2))

    exts = []

    for key, group in groupby(temp_exts, lambda ext: re.search('^(.+)\.(.+)$', ext).group(2)):
        exts += sorted(list(group))

    return names + exts


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == [
        '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == [
        '1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == [
        '.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == [
        '.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == [
        '1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == [
        '1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
