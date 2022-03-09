def anagram(s1: str, s2: str) -> bool:
    dict_letters = {}
    s1, s2, = s1.replace(' ', '').lower(), s2.replace(' ', '').lower()

    for i in range(0, len(s1)):
        if s1[i] in dict_letters:
            dict_letters[s1[i]] += 1
        else:
            dict_letters[s1[i]] = 1

    for i in range(0, len(s2)):
        if s2[i] in dict_letters and dict_letters[s2[i]] > 0:
            dict_letters[s2[i]] -= 1
            if dict_letters[s2[i]] == 0:
                del dict_letters[s2[i]]
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


