a_list=[]
multiply=1
for x in range(0,13):
    user_input = int(input("please enter a number: ")) 
    a_list.append(user_input)
for cn in range(0,len(a_list)-1):
    cnn=a_list[cn]
    print(cnn)
    multiply=multiply*cnn
print(multiply)
