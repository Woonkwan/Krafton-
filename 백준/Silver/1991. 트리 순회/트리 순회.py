import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data,left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def pre(node):
    print(node.data, end = '')
    if node.left != None:
        pre(tree[node.left])
    if node.right != None:
        pre(tree[node.right])

def ino(node):
    if node.left != None:
        ino(tree[node.left])
    print(node.data, end = '')
    if node.right != None:
        ino(tree[node.right])

def pos(node):
    if node.left != None:
        pos(tree[node.left])
    if node.right != None:
        pos(tree[node.right])
    print(node.data, end = '')

#전위 중위 후회 순으로 함수 정의

tree = {}

N  = int(input())

for _ in range(N):
    x, y, z = input().split()
    if y == '.':
        y = None
    if z == '.':
        z = None
    tree[x] = Node(x, y, z)
#N을 받아서 N만큼 정보를 받음.


#출력
pre(tree['A'])
print()

ino(tree['A'])
print()

pos(tree['A'])
print()