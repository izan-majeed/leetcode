class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add(num1, num2, c):
    s = num1 + num2 + c
    if s>9:
        c = s//10
        s = s%10
        return s, c
    return s, 0

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        s, carry = add(l1.val, l2.val, carry)
        l3 = ListNode(s)
        temp1 = l1.next
        temp2 = l2.next
        temp3 = l3

        while (temp1 or temp2) or carry !=0:
            if (not temp1) and (not temp2):
                temp3.next = ListNode(carry)
                break
            elif not temp1:
                s, carry = add(temp2.val, 0, carry)
                temp3.next = ListNode(s)
                temp2 = temp2.next
                temp3 = temp3.next
            elif not temp2:
                s, carry = add(temp1.val, 0, carry)
                temp3.next = ListNode(s)
                temp1 = temp1.next
                temp3 = temp3.next
            else:
                s, carry = add(temp1.val, temp2.val, carry)
                temp3.next = ListNode(s)
                temp1 = temp1.next
                temp2 = temp2.next
                temp3 = temp3.next

        return l3

