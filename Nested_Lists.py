if __name__ == '__main__':
    actuallist = []
    namelist = []
    scorelist = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        namelist.append(name)
        scorelist.append(score)
        actuallist.append([name,score])
    
    n = len(actuallist)
    scoreset = set(scorelist)
    scorelist = list(scoreset)
    rmv = min(scorelist)
    scorelist.remove(rmv)
    
    secondmin = min(scorelist)
    
    storelist = []
    for i in range(n):
        if (float(actuallist[i][1])==secondmin):
            storelist.append(actuallist[i][0])
    
    storelist.sort()
    m = len(storelist)
    for i in range(m):
        print(storelist[i])
