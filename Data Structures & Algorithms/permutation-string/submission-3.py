class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        m = len(s1)
        n = len(s2)
        if m>n:
            return False

        for i in range(m):
            count1[ord(s1[i])-97] +=1
            count2[ord(s2[i])-97] +=1

        if count1 == count2:
            return True
        
        for i in range(m, n):
            count2[ord(s2[i])-97] += 1
            count2[ord(s2[i-m])-97] -= 1
            if count1 == count2:
                return True

        return False