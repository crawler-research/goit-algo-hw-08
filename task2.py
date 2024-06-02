from avl_tree import *

root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = insert(root, key)
    print("Вставлено:", key)
    print("AVL-Дерево:")
    print(root)


def find_min(node):
    current = node
    while(current.left):
        current = current.left
    return current.key

print("МІНІМАЛЬНЕ ЗНАЧЕННЯ:", find_min(root))  # -1