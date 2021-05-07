# Enter your code here. Read input from STDIN. Print output to STDOUT
l = input().split() 
N = int(l[0])
M = 3*N

mid = int(N/2)
num = 0

for i in range(N):
    if i<mid:
        num = (2*i+1)
        print((num*'.|.').center(M,'-'))
    elif i==mid:
        print('WELCOME'.center(M,'-'))
    else:
        print( (num*'.|.').center(M,'-') )
        num = num - 2
