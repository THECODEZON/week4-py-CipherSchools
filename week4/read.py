f = open('file.text')
print(f'cursor position - {f.tell()}')
print(f.read())
print(f'cursor position - {f.tell()}')
print(f.read())
f.close()

lines = f.readlines()
print(len(lines))

with open('file.text') as f:
    data = f.read()
    print(data)

print(f.closed)