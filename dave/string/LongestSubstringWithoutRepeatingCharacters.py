class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        ms = None
        ts = ''
        for i in range(len(s)):
            if s[i] in ts:
                ts = ts[ts.find(s[i]) + 1:]
            ts += s[i]
            if ms is None or len(ts) > len(ms):
                ms = ts
        if ts and len(ts) > len(ms):
            ms = ts
        return len(ms)


def main():
    sol = Solution()

    test_cases = [
        "",
        "abcabcbb",
        "bbbb",
        "hnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcac",
    ]
    for test_case in test_cases:
        import time
        a = time.time()
        ret = sol.lengthOfLongestSubstring(test_case)
        b = time.time()
        print b - a, ret , test_case

if __name__ == "__main__":
    main()
