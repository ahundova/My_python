'''
#print('hello')
a=2
b=7
c=12
#print(f'1-{a}  2-{b} 3-{c}')
print("1{} 2{} 3{}". format(a,b,c))'''
# минимальный делитель числа
n=int(input())
flag=True
i=2
while flag:
    if n%i==0:
        flag=False
        print(i)
    elif i>n//2:
        print(n)
        flag=False
    i+=1

        