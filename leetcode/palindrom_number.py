def is_palindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    return False


print(is_palindrome(20002))
