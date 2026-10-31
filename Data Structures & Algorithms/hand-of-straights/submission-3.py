class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = defaultdict(int)
        for value in hand:
            count[value] = count.get(value, 0) + 1
        
        # count = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
        # 1,2,2,3,3,4,4,5

        for card in sorted(hand):
            c = count[card]
            for next_card in range(card, card+groupSize):
                if count[next_card] < c:
                    return False
                count[next_card] -= c

        return True





