
# Saving value the range of 2000~3200 -> multiple of '7' && !multiple of '5'
list=[(a) for a in range(2000,3200) 
    if a%7==0 
       if a%5!=0
       ]

print (list)

