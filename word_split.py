def word_split(s, wordDict):
    n = len(s)
    soulutions = {}
    soulutions[n] = ['']
    min_len = max([len(word) for word in wordDict])
    def solve(i):
        if i not in soulutions:
            soulutions[i] = [s[i:j] + (tail and (' ' + tail))
                            for j in range (i, n+1)
                            if s[i:j] in wordDict
                            for tail in solve(j)]
        return soulutions[i]

    solve(0)
    return soulutions[0]

wordDict = set(["face", "book", "bo", "ok"])
print(word_split('facebook', wordDict))
