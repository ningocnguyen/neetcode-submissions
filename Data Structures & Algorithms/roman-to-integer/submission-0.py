class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        n = len(s)
        total = 0

        for i in range(n):
            current_val = roman_map[s[i]]
            if i+1 < n and current_val < roman_map[s[i+1]]:
                total -= current_val
            else:
                total += current_val
        
        return total
