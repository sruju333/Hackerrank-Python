def mutate_string(string, position, character):
    #convert string to list
    l = list(string)
    l[position] = character
    #convert list back to string using .join()
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
