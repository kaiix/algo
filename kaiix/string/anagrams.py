#  https://leetcode.com/problems/anagrams/


def anagrams(strs):
    from collections import defaultdict
    groups = defaultdict(list)
    for s in strs:
        groups[''.join(sorted(s))].append(s)
    result = []
    for group in groups.itervalues():
        if len(group) > 1:
            result.extend(group)
    return result


def anagrams_once(strs):
        groups = {}
        result = []
        for i in xrange(len(strs)):
            s = ''.join(sorted(strs[i]))
            if s not in groups:
                groups[s] = i
            else:
                if groups[s] >= 0:
                    result.append(strs[groups[s]])
                    groups[s] = -1
                result.append(strs[i])
        return result


if __name__ == '__main__':
    print anagrams_once(['tea', 'and', 'ate', 'eat', 'dan'])
