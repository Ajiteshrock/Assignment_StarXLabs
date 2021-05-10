def compare_strings(l:list):
    s1 = l[0].lower()
    s2 = l[1].lower()
    flag = 1
    for i in s2:
        if i in s1:
            flag = 0
            pass
        elif i not in s1:
            flag=1
            break
    if flag==0:
        return "Yes"
    else:
        return "No"
        