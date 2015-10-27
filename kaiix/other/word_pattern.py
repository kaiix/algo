#  https://leetcode.com/problems/word-pattern/


def wordPattern(pattern, s):
    parts = s.split()
    if len(pattern) != len(parts):
        return False
    table = {x: None for x in set(pattern)}
    for w, p in zip(parts, pattern):
        if not table[p]:
            if w in table.values():
                return False
            else:
                table[p] = w
        elif table[p] != w:
            return False
    return True


if __name__ == '__main__':
    print wordPattern('abab', 'bar foo bar foo')
