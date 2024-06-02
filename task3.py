from avl_tree import *

root = None
keys = [10, 20, 30, 25, 28, 27, -1]
for key in keys:
    root = insert(root, key)
    print("Вставлено:", key)
    print("AVL-Дерево:")
    print(root)

def sum_values(node):
    if node is None:
        return 0
    else:
        return node.key + sum_values(node.left) + sum_values(node.right)

sum_values(root)  # 139
