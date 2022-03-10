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