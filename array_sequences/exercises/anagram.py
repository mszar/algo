def anagram(s1: str, s2: str) -> bool:
    dict_letters = {}
    s1, s2, = s1.replace(' ', '').lower(), s2.replace(' ', '').lower()

    for pos, item in enumerate(s1):
        if s1[pos] in dict_letters:
            dict_letters[s1[pos]] += 1
        else:
            dict_letters[s1[pos]] = 1

    for pos, item in enumerate(s2):
        if s2[pos] in dict_letters and dict_letters[s2[pos]] > 0:
            dict_letters[s2[pos]] -= 1
            if dict_letters[s2[pos]] == 0:
                del dict_letters[s2[pos]]
        else:
            return False

    if not bool(dict_letters):
        return True
    return False



print(anagram('go go go', 'gggooo'))
print(anagram('abc', 'cba'))
print(anagram('hi man', 'hi     man'))
print(anagram('aabbcc', 'aabbc'))
print(anagram('123', '1 2'))
