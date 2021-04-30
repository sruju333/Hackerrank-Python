if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arraylist = list(arr) #convert map to list
    arrayset = set(arraylist) #convert list to set to remove duplicates
    arraylist = list(arrayset) #convert set back to list
    
    arraylist.remove(max(arraylist))
    print(max(arraylist))
