s = input()

#flags
alnum_flag = False
alpha_flag = False
digit_flag = False
low_flag = False
up_flag = False

for x in s:
    if (x.isalnum()):
        alnum_flag = True
    if (x.isalpha()):
        alpha_flag = True
    if (x.isdigit()):
        digit_flag = True
    if (x.islower()):
        low_flag = True
    if (x.isupper()):
        up_flag = True

print(alnum_flag)
print(alpha_flag)
print(digit_flag)
print(low_flag)
print(up_flag)
