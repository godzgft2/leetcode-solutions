#LeetCode: 2095. Delete the Middle Node of a Linked List
#Runtime: 635ms, Beats 23.42%
#Memory: 50.25MB, Beats 95.36%

def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head.next == None:
        del head
        return
    current = head
    remove = head
    count = 1
    while current.next != None:
        current = current.next
        count += 1
    for i in range(count//2-1):
        remove = remove.next

    if remove.next != None:
        temp = remove.next
        remove.next = remove.next.next
        del temp
    else:
        del remove.next

    return head
