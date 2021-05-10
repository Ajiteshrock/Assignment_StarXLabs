from First_Queston import get_checkout_time

d = {'1':[[5,1,3],1],
     '2':[[10,3,4,2],2],
     '3':[[10,2,3,4,6,7,8,9],3]}
c=0
for i in d.keys():
    c+=1
    print("Minimum Time Taken for line "+str(c)+" "+str(get_checkout_time(d[i][0] , d[i][1]))+" minutes")

print("\nSecond question testing")
from Second_question import compare_strings

l = [['hello','Hello'],['Hello','hey'],['Alien','line'],['Ajitesh','Ashish']]

for i in l:
    print(compare_strings(i))