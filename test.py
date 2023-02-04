if __name__ == '__main__':
    list1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
    min1 = 0
    min2 = 0

    for i in range (len(list1)):
        
        if min1<list1[i][1]:
            min1=list1[i][1]
    
    for i in range (len(list1)):
        if min2<list1[i][1] and min1!=list1[i][1]:
            min2=list1[i][1]

    
print(min2)

        