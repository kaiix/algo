#  https://leetcode.com/problems/length-of-last-word/


def lengthOfLastWord(s):
    count = 0
    sep = False
    for i in s:
        if i == ' ':
            sep = True
        else:
            if sep:
                count = 0
                sep = False
            count += 1
    return count


if __name__ == '__main__':
    print lengthOfLastWord('hello, world')
    print lengthOfLastWord('hello, ')
    print lengthOfLastWord('hello, world  ')
