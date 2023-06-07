from typing import List
values = [1, 2, 3, 4, 5]


def plus_one(digits: List[int]) -> List[int]:
    return [int(x) for x in str(int(''.join(map(str, digits))) + 1)]


print(plus_one(values))
