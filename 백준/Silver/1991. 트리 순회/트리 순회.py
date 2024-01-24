import sys
input = sys.stdin.readline



#=================================
def first(node):
    if node == None:
        return
    print(node, end = '')
    first(tree[node][0])
    first(tree[node][1])
#=================================
def mid(node):
    if node == None:
        return
    mid(tree[node][0])
    print(node, end = '')
    mid(tree[node][1])
#=================================
def last(node):
    if node == None:
        return
    last(tree[node][0])
    last(tree[node][1])
    print(node, end = '')

#=================================입력

N = int(input())
tree = {}

for _ in range(N):
    x, y, z = input().split()
    tree[x] = (y if y != '.' else None, z if z != '.' else None)

#=================================출력
first('A')
print()

mid('A')
print()

last('A')
print()