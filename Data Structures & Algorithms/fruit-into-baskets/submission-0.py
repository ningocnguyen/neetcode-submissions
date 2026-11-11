class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        curr = 0
        max_fruit = 0
        # keep a window of max 2 count for each type of fruit
        # iterate thru each fruit
        # when hit count(type of fruit) > 2: narrow the window from the left
        # keep track of max fruits in every iteration
        l=0
        count = defaultdict(int)
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            curr += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l+=1
                curr -= 1
            max_fruit = max(curr, max_fruit)
        
        return max_fruit