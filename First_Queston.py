def get_checkout_time(l:list, num_reg:int):
    queue = [None] * num_reg
    if num_reg==1:
        return sum(l)
    else:
        min_time = 0
        count_= 0
        for i in range(num_reg):
            queue[i] = l[i]
            count_= i
        for j in range(count_+1,len(l)):
                min_ = min(queue)
                min_time+=min_
                for i in range(len(queue)):
                    queue[i] = queue[i] - min_
               
                min_ = min(queue)
                ind = queue.index(min_)
                queue[ind] = l[j]
        min_time = min_time + max(queue)
       
        return min_time
#first test_case
#time_checkout = get_checkout_time([5,1,3],1)
#print(time_checkout)

#second test_case
#time_checkout = get_checkout_time([10,3,4,2],2)
#print(time_checkout)

# custom test case having three cash registers
#time_checkout = get_checkout_time([10,2,3,4,6,8,9],3)
#print(time_checkout)
# Answer - 18minutes
