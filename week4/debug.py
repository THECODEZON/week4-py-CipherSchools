import pdb

pdb.set_trace()
name = input('Please type your name')
age = input('Please type your age: ')
print(f'hello{name} your age is {age}')
age2 = int(age) + 5
print(f'{name} you will be {age2} in next five years')