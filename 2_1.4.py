def print_get(a, b):
    if b in namespaces[a]['variables']:
        return a
    else:
         if a == 'global' and b not in namespaces[a]['variables']:
             return None
         else:
            return print_get(namespaces[a]["parent"], b)
n = int(input())
namespaces = {
    'global': {
        'variables': [],
        'parent': None
    }
}
for i in range(n):
    x = [i for i in input().split()]
    if x[0] == "create":
        namespaces[x[1]] = {'variables': [], 'parent': x[2]}
    if x[0] == "add":
        namespaces[x[1]]['variables'].append(x[2])
    if x[0] == 'get':
        print(print_get(x[1], x[2]))
