class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        max_f = 0
        
        for r in range(len(s)):
            # Cập nhật tần suất ký tự bên phải
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(max_f, count[s[r]])
            
            # Nếu (độ dài cửa sổ - ký tự phổ biến nhất) > k: cửa sổ vi phạm
            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
                # Lưu ý: Không cần cập nhật lại max_f ở đây
                
            res = max(res, r - l + 1)
            
        return res