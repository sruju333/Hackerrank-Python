def swap_case(s):
    ns = ""
    for val in s:
        if (val.isupper()==True):
            val = val.lower()
            ns += val
        else:
            val = val.upper()   
            ns += val
    return ns

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
