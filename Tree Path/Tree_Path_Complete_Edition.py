def find_path(node, target_sum, current_sum, path, tree, parent):
    if node is None:
        return None
    current_sum += node
    path[0].append(node)
    path[1].append(parent)
    if current_sum == target_sum:
        return path
    if not tree:
        if current_sum == target_sum:
            return path
        else:
            return None
    for child in range(len(tree[0])):
        if child == parent * 2 or child == parent * 2 + 1:
            found_path = find_path(tree[0][child], target_sum, current_sum, [path[0][:], path[1][:]], tree[1:], child)
            if found_path:
                return found_path
    return None


# Вывод дерева с отмеченным путём (если путь найден, если нет, просто вывод дерева)
def tree_illustrator(tree, depth, path):
    for i in range(depth):
        n = len(tree[i])
        spaces_between = 2 ** (depth - i + 1) - 1
        spaces_around = 2 ** (depth - i) - 1
        print(' ' * spaces_around, end='')
        for j in range(n):
            if tree[i][j] is not None:
                print(tree[i][j], end='')
                if path and i < len(path[0]):
                    if path[1][i] == j:
                        print('*', end='')
            else:
                print('', end='')
            if j < n - 1:
                print(' ' * spaces_between, end='')
        print()

def insert_none(tree):
    k = -2
    list = tree[k]
    for i in range(len(list)):
        if list[i] == None:
            tree[k+1].append(None)
            for j in range(len(tree[k+1]) - 1, i+1, -1):
                tree[k+1][j] = tree[k+1][j - 1]
            tree[k + 1][i+1] = None
            tree[k+1].append(None)
            for j in range(len(tree[k+1]) - 1, i+1, -1):
                tree[k+1][j] = tree[k+1][j - 1]
            tree[k+1][i+1] = None
    return tree

print("Введите целевую сумму:")
target_sum = int(input())
tree = []
print("Введите строку, описывающую древо:")
a = [int(x) if x else None for x in input().split(',')]
n = len(a)
# Счётчики какик-то
i = 0
q = 0
j = 0
k = 0
l = 0
# Создание списка "слоёв" дерева
while i < n:
    b = []
    if l:
        b = a[l:2*l+1]
    row = a[i:2*i+1]
    tree.append([])
    if l:
        for g in range(len(b)):
             if b[g] == None:
                 tree[j] += (None for p in range(2))
             else:
                 tree[j].append(row[k])
                 tree[j].append(row[k + 1])
                 k = k + 2
    tree[j] += row[k:]
    k = 0
    l = i
    i = 2*i+1
    j += 1
i = 0
for i in range(len(tree)):
    if len(tree[i]) > 2 ** i:
        a = tree[i][:2 ** i]
        b = tree[i][2 ** i:]
        print(a, b)
        tree.append(None)
        for j in range(len(tree) - 1, i, -1):
            tree[j] = tree[j - 1]
        tree[i] = a
        tree[i + 1] = b
i = 0
tree = insert_none(tree)
# Заполнение пустот
if len(tree[-1]) != 2 ** ((len(tree) - 1)):
    for i in range(len(tree[-1]), 2 ** (len(tree) - 1), 1):
        tree[-1].append(None)

path = find_path(tree[0][0], target_sum, 0, [[],[]], tree[1:], 0)



# Вывод пути
if path:
    print("Найден путь:")
    n = len(path[0])
    for i in range(n):
        if n - i - 1:
            print(path[0][i], "->", end=' ')
        else:
            print(path[0][i])
else:
    print("Путь не найден.")

# Изображение дерева
print("\n","preAlpha-версия Tree Illustrator 3000")
tree_illustrator(tree, len(tree), path)
