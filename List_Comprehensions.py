if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    #Create and initialize an empty list
    list = [] 
   
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if ((i+j+k)==n):
                    pass
                else:
                    list = list + [[i,j,k]]
                
    print(list) 
