class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # pair position and speed
        cars = list(zip(position, speed))

        # sort by position descending
        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:

            # time to reach target
            time = (target - pos) / spd

            # new fleet
            stack.append(time)

            # merge fleets
            if len(stack) >= 2 and stack[-1] <= stack[-2]:

                # current fleet merges with front fleet
                stack.pop()

        return len(stack)
