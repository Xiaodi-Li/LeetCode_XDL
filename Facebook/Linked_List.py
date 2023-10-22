# 138. Copy List with Random Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Random_Pointer:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        m = {}
        curr = m[head] = Node(head.val)
        ans = curr

        while head:
            if head.random:
                if head.random not in m:
                    m[head.random] = Node(head.random.val)
                curr.random = m[head.random]

            if head.next:
                if head.next not in m:
                    m[head.next] = Node(head.next.val)
                curr.next = m[head.next]

            head = head.next
            curr = curr.next

        return ans

# 708. Insert into a Sorted Circular Linked List
# Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.
#
# If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.
#
# If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Sorted_Circular_Linked_List:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal, None)
            node.next = node
            return node
        head_res = head
        prev = head
        curr = head.next

        while True:
            if prev.val <= insertVal <= curr.val or (
                    prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val)) or prev == curr:
                prev.next = Node(insertVal, curr)
                break
            prev = prev.next
            curr = curr.next
            if prev == head:
                prev.next = Node(insertVal, curr)
                break

        return head_res

# 426. Convert Binary Search Tree to Sorted Doubly Linked List
# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
#
# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
#
# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Sorted_Doubly_Linked_List:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        dummy = Node(0, None, None)
        prev = dummy
        stack, node = [], root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right

        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right
