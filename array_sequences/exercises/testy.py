
def pair_sum(arr: list, k: int) -> int:
    results: list = []
    while len(arr) > 0:
        x = arr.pop()
        for pos, item in enumerate(arr):
            if x + item == k:
                del arr[pos]
                results.append((x, item))
        result = len(results)
        return result



print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(pair_sum([1,2,3,1],3))
print(pair_sum([1,3,2,2],4))