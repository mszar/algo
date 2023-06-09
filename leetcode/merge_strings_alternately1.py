
def mergeAlternately(word1: str, word2: str) -> str:
    word_chain = ""
    n = max(len(word1), len(word2))
    for x in range(n):
        if x < len(word1):
            word_chain += word1[x]
        if x < len(word2):
            word_chain += word2[x]
    return word_chain

word1 = "abcdefgh"
word2 = "1234"

print(mergeAlternately(word1, word2))
