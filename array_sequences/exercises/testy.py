
def pair_sum(arr: list, k: int) -> int:

    x = arr.pop()

    def _check_values(x, arr):
        results: list = []
        for pos, item in enumerate(arr):
            if x + item == k:
                del arr[pos]
                results.append((x, item))
                print(results)

    for i in range(0, len(arr)):
        print(_check_values(x, arr))





lst = [1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1]
value = 10

print(pair_sum(lst, value))
