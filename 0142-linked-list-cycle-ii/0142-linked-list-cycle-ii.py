# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # edge case: empty list ya single node → cycle possible nahi
        if not head or not head.next:
            return None
        
        slow = head   # 1 step pointer
        fast = head   # 2 step pointer

        # Step 1: detect cycle (Floyd’s Algo)
        while fast and fast.next:
            slow = slow.next          # move 1 step
            fast = fast.next.next     # move 2 steps

            # agar dono mil gaye → cycle exist karti hai
            if slow == fast:

                # Step 2: find cycle start
                slow = head   # slow ko reset kar diya head pe

                # ab slow & fast dono 1 step se chalenge
                # jahan milenge = cycle ka starting node
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow   # cycle start node

        # agar kabhi mile hi nahi → no cycle
        return None