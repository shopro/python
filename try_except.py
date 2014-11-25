


while(1): #Infinite loop that is stating for verifying Error

    try:
        val = [int(a) for a in input("Enter Two numbers(but, second number is not'Zero'): ").split(',')]
        result = val[0] / val[1]
        break #Above Condition is True, Break Loop

    except ZeroDivisionError: # When Second number is entered '0'
        print("Second number can't be 'Zero'!!")

    except ValueError: # When Something not proper value(numbers) is entered
        print("It is not proper Value!!")
   
print (result)

