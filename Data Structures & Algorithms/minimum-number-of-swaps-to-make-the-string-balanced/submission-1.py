class Solution:
    def minSwaps(self, s: str) -> int:
        max_imbal = 0
        balance = 0

        for br in s:
            if br == "]":
                balance -= 1
                if -balance > max_imbal:
                    max_imbal = -balance
            else:
                balance += 1

        return (max_imbal + 1) // 2

