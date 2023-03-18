""" LAB 04 - 01/31/23
Binary Search Trees - Sterling Miller
"""


class Node:
    """ Abstract Class for Creating a Node """
    def __init__(self, node_data: int):
        self.node_data = node_data

    def __str__(self):
        raise NotImplementedError('Refer to the correct type')

    def sum_node_data(self):
        raise NotImplementedError('Refer to the correct type')


class Leaf(Node):
    """ Creates a Child Node """
    def __init__(self, node_data: int):
        super().__init__(node_data)

    def __str__(self):
        return f'{self.node_data}'

    def sum_node_data(self):
        return self.node_data


class Internal(Node):
    """ Creates a Parent Node """
    def __init__(self, node_data: int, right: Node, left: Node):
        self.right = right
        self.left = left
        super().__init__(node_data)

    def __str__(self):
        return f'< {self.node_data}, {self.right}, {self.left} >'

    def sum_node_data(self):
        return self.node_data + self.right.sum_node_data() + self.left.sum_node_data()


def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7, l2, l3)
    root = Internal(5, l1, i)
    print(root)
    print(root.sum_node_data())


if __name__ == '__main__':
    main()
