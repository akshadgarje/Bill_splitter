import random

x = {}
m = []
print("Enter the number of friends joining (including you):")
a = int(input())
print()
if a <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(a):
        b = input()
        m.append(b)
        x[b] = 0
    print("Enter the total bill value:")
    c = int(input())
    z = round(c / a, 2)
    for i in x:
        x[i] = z
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    d = input()
    print()
    if d == 'Yes':
        n = random.choice(m)
        print(f"{n} is the lucky one!")
        o = round(c / (a - 1), 2)
        for i in x:
            if i == n:
                x[i] = 0
            else:
                x[i] = o
        print(x)            
    elif d == 'No':
        print("No one is going to be lucky")
        print(x)