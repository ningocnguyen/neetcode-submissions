class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net_gas = 0
        start = 0
        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            net_gas += gas[i] - cost[i]
            if net_gas < 0:
                start = i+1
                net_gas = 0
                

        return start
            