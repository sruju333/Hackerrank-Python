if __name__ == '__main__':
    N = int(input())
    l = []
    s = []
    for _ in range(N):
        l = input().split()
        if (l[0]=="insert"):
            s.insert(int(l[1]), int(l[2]))
        elif (l[0]=="remove"):
            s.remove(int(l[1]))
        elif (l[0]=="append"):
            s.append(int(l[1]))
        elif (l[0]=="sort"):
            s.sort()
        elif (l[0]=="pop"):
            s.pop()
        elif (l[0]=="reverse"):
            s.reverse()
        else:
            print(s)    
