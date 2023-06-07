
def mergeAlternately(word1: str, word2: str) -> str:
    word_chain = ""
    n = min(len(word1), len(word2))
    for x in range(n):
        word_chain += word1[x]
        word_chain += word2[x]
    word_chain += word1[n:]
    word_chain += word2[n:]


word1 = "abdc"
word2 = "pqeeeeee"

mergeAlternately(word1, word2)
