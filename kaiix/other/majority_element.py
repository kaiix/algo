#  https://leetcode.com/problems/majority-element/


def majorityElement2(nums):
    counter = {}
    for n in nums:
        if n in counter:
            counter[n] += 1
        else:
            counter[n] = 1
    return max(counter, key=lambda x: counter[x])


#  http://www.cs.utexas.edu/~moore/best-ideas/mjrty/index.html

def majorityElement(nums):
    count = 0
    candidate = None
    for i in nums:
        if count == 0:
            candidate = i
            count += 1
        else:
            if i == candidate:
                count += 1
            else:
                count -= 1
            if count > len(nums)/2+1:
                break
    return candidate


if __name__ == '__main__':
    print majorityElement([2, 1, 3, 2, 2, 3])
