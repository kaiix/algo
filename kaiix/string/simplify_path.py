# https://leetcode.com/problems/simplify-path/


def simplifyPath(path):
    stack = []
    part = ''
    if path[-1] != '/':
        path += '/'

    for ch in path:
        if ch == '/':
            if part == '' or part == '.':
                continue
            elif part == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(part)
            part = ''
        else:
            part += ch

    return '/'+'/'.join(stack)


if __name__ == '__main__':
    print simplifyPath('/home/')
    print simplifyPath('/a/./b/../../c/')
