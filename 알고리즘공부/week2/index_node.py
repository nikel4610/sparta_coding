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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index): #인덱스 번째에 노드 넣기
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value): #인덱스 번째에 새로운 원소 넣기 / 몇번쨰에 어떤값 넣을지
        new_node = Node(value) # [6]

        if index == 0: # 0번째는 -1이 되기 때문에 따로 처리
            new_node.next = self.head # [6] -> [5]
            self.head = new_node #head-> [6] -> [5] -> ...
            return

        node = self.get_node(index - 1) # [5]
        next_node = node.next #[12]
        node.next = new_node #[5] -> [6]
        new_node.next = next_node #[6] -> [12]
        return

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(1, 6)
linked_list.print_all()
