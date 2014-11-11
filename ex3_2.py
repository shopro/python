from operator import itemgetter

# 'val' is a group that is 'list' defined python
#about Entering Some informations constructed by tuple
#set off a clause by a comma
val = [tuple(input("Enter a value : ").split(','))]


i=1 #count

while i<5: # For extending 'list' construckted by tuple
    i=i+1
    val.extend([tuple(input("Enter a value : ").split(','))])
    

# index '0' of itemgetter is indicating 'first value' in certain 'list'
name = itemgetter(0) 


#Sorting 'val' on the standard of 'Name'
print(sorted(val, key=name))


    
