def removeDuplicatesPreserveOrder(nums: list[int]) -> list[int]:
    seen = set()
    result = []

    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)

    return result