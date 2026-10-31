class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = defaultdict(int)
        for value in hand:
            count[value] = count.get(value, 0) + 1
        
        # count = {1: 1, 2: 2, 3: 2, 4: 2, 5: 1}

        unique_card = sorted(count.keys())

        for card in sorted(unique_card):
            c = count[card]
            for next_card in range(card, card+groupSize):
                if count[next_card] < c:
                    return False
                count[next_card] -= c

        return True





