def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    if str(x) == str(x)[::-1]:
        return True
    return False

def is_palindrome_2(x: int) -> bool:
    if x < 0:
        return False
    return str(x) == str(x)[::-1]


print(is_palindrome(-20002))
print(is_palindrome_2(20002))
