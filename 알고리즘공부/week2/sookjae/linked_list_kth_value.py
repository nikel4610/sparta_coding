class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        #1. 길이 알아내고 구하기
        #length = 1 #길이 변수
        #cur = self.head

        #while cur.next is not None:
        #    cur = cur.next #cur을 계속 다음 cur로 보낸다
        #    length += 1 #길이 +1

        #end_length = length - k
        #cur = self.head

        #for i in range(end_length):
        #    cur = cur.next

        #return cur

        #2. 길이에서 k만큼 뺀 길이만큼 이동
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
