class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pst, spd in cars:
            time = (target-pst) / spd
            if stack and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack)
