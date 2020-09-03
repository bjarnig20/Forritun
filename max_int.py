
num_int = int(input("Input a number: "))    # Do not change this line
sum_1 = 0
sum_2 = 0
while num_int > 0:
    sum_1 = num_int
    if sum_1 > sum_2:
        sum_2 = sum_1
    else:
        num_int = int(input("Input a number: "))

    

print("The maximum is", sum_2) 

# Fill in the missing code

