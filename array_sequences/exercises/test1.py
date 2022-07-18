def anagram(s1: str, s2: str) -> bool:
    s1, s2, = s1.replace(' ', '').lower(), s2.replace(' ', '').lower()
    return (sorted(s1) == sorted(s2))


print(anagram('Go Go Go', 'gggooo'))
print(anagram('abc', 'cba'))
print(anagram('hi man', 'hi     man'))
print(anagram('aabbcc', 'aabbc'))
print(anagram('123', '1 2'))
