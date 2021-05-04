def count_substring(string, sub_string):
    teststring = string
    count = 0
    pos = 0
    while pos!=-1:
        pos = teststring.find(sub_string)
        if pos>=0:
            count = count + 1
        l = list(teststring)
        l[pos] = 'x' #replace character with x
        teststring = ''.join(l)
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
