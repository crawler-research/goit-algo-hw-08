from avl_tree import *

root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = insert(root, key)
    print("Вставлено:", key)
    print("AVL-Дерево:")
    print(root)


def find_max(node):
    current = node
    while(current.right):
        current = current.right
    return current.key

print("МАКСИМАЛЬНЕ ЗНАЧЕННЯ:", find_max(root))  # 30