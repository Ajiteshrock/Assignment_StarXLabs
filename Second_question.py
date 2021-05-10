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
        
#second approach 

'''def match_letters(l:list):
    s1 = list(l[0].lower())
    s2 = list(l[1].lower())
    s1 = set(s1)
    s2 = set(s2)
    if s1.intersection(s2) == s2:
        return "Yes"
    else:
        return "No"

print(match_letters(['ajitesh','ashish']))''''