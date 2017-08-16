a_list=[12,32,22,43,63,13,75,73,82,95,73,52,32,12]
coc=0
cr=0
for oe in a_list:
    if oe%2==0:
        coc=coc+1
    else:
        cr=cr+1
print(coc)
print(cr)
if coc>cr:
    print"even number is more"
elif cr>coc:
    print"odd number is more"
else:
    print"both are equal"
