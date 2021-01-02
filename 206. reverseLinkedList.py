class Solution:
    def reverseList(self, head):
        if head:
            current = head
            prev = None
            next_ = head.next

            while current.next:
                current.next = prev
                prev = current
                current = next_
                next_ = next_.next
            current.next = prev
            return current