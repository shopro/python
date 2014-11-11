#factorial.py

val = input("Enter number: ") # val is a variable that is saving 'one number'
result =1

while val != 0: # if val equals '0', loop break
    result = result * val
    val=val-1


print (result)
