# 1-misol
# def smallestEvenMultiple(n: int) -> int:
#     return 2 * n if n % 2 == 1 else n
# print(smallestEvenMultiple(13))
from typing import List


# oson matematik logika. Kommentga olmasam o'zgaruvhilar va funksiyalarda xatolik chalkashlik bo'lishi mumkin
# 2-masala
# def sortPeople(names: List[str], heights: List[int]) -> List[str]:
#     dict_hn = {h: n for h, n in zip(heights, names)}
#     heights.sort(reverse=True)
#     return [dict_hn[h] for h in heights]
#
# print(sortPeople(["Mary","John","Emma"], [180,165,170]))


class LUPrefix:

    def __init__(self, n):
        self.data = [0]*n
        self.res = 0

    def upload(self, video):
        self.data[video-1] = 1

    def longest(self):
        while self.res < len(self.data) and self.data[self.res] == 1:
            self.res += 1

        return self.res



