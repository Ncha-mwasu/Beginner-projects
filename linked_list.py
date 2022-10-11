class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Empty list")
            return

        itr = self.head
        listr = ''

        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)


if __name__ == '__main__':
    li = LinkedList()
    li.insert_beginning(5)
    li.insert_beginning(89)
    li.print()
