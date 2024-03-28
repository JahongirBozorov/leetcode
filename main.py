# def countPoints(rings: str) -> int:
#     set_B = set()
#     set_G = set()
#     set_R = set()
#     for i, each in enumerate(rings):
#         if each == 'B':
#             set_B.add(rings[i + 1])
#         elif each == 'R':
#             set_R.add(rings[i + 1])
#         elif each == 'G':
#             set_G.add(rings[i + 1])
#         else:
#             continue
#     return len(set_B.intersection(set_R.intersection(set_G)))
#
# print(countPoints("B0B6G0R6R0R6G9"))
from typing import List


#     2- misol


# def firstPalindrome(words: List[str]) -> str:
#     for i in words:
#         if i == i[::-1]:
#             return i
#     return ""
#
# print(firstPalindrome(["abc","car","ada","racecar","cool"]))


#   3- misol

def mostWordsFound(sentences: List[str]) -> int:
    list1 = []
    for i in sentences:
        list1.append(len(i.split(" ")))
    return max(list1)

print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))