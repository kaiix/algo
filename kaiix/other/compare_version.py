def compareVersion(version1, version2):
    if version1 == version2:
        return 0

    v1 = map(int, version1.split('.'))
    v2 = map(int, version2.split('.'))
    l1 = len(v1)
    l2 = len(v2)
    i = 0
    while True:
        if v1[i] > v2[i]:
            return 1
        elif v1[i] < v2[i]:
            return -1
        else:
            i += 1
            if i >= l1 and i >= l2:
                return 0
            elif i >= l1:
                if any(v2[i:]):
                    return -1
                else:
                    return 0
            elif i >= l2:
                if any(v1[i:]):
                    return 1
                else:
                    return 0


if __name__ == '__main__':
    print compareVersion('01', '1')
    print compareVersion('01.2', '1.30')
    print compareVersion('1', '1.0')
