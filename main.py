from typing import List

# 1-misol
# def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
#     if m * n != len(original):
#         return []
#
#     matrix = [[] for i in range(m)]
#     curr = 0
#
#     for i in range(m):
#         for j in range(n):
#             matrix[i].append(original[curr])
#             curr += 1
#     return matrix
#
#
# print(construct2DArray([1, 2, 3], 1, 3))


# 2-misol

# def minimumPerimeter(neededApples: int) -> int:
#     total = 0
#     for i in range(neededApples):
#         total += 12 * (i + 1) * (i + 1)
#         if total >= neededApples:
#             return 8 * (i + 1)
#
#
# print(minimumPerimeter(1))



# 3-misol

def canBeTypedWords(text: str, brokenLetters: str) -> int:
    l = text.split()
    c = 0
    for i in l:
        for b in brokenLetters:
            if b in i:
                c += 1
                break
    return len(l) - c


print(canBeTypedWords("Hello World", "ad"))