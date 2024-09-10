#LeetCode: 2807. Insert Greatest Common Divisors in Linked List
#Runtime: 66ms, Beats 76.48%
#Memory: 19.54MB, Beats 79.95%

#Inserts the GCD of the values of two nodes as a new node in between the nodes in a linked list

def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    while curr.next:
        new_val = gcd(curr.val, curr.next.val)
        node = ListNode()
        node.val = new_val
        node.next = curr.next
        curr.next = node
        curr = curr.next.next
    return head
