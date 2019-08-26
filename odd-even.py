a_list=[]
coc=0
cr=0
for x in range(0,13):
    user_input = int(input("please enter a number: ")) 
    a_list.append(user_input)
for oe in a_list:
    if oe%2==0:
        coc=coc+1
    else:
        cr=cr+1
print(coc)
print(cr)
if coc>cr:
    print("even numbers are more")
elif cr>coc:
    print("odd numbers are more")
else:
    print("both are equal")
