# Write your solution here
def list_sum(list1, list2):

    list_sum2 =[]

    for i in range(len(list1)):

        list_sum2.append(list1[i] + list2[i])
        
    return list_sum2


#main code 

if __name__ == "__main__":
    a = [1,2,3]
    b = [7,8,9]

    print(list_sum(a,b))
