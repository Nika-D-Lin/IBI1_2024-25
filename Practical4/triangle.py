'''
We have learned that this kind of series have a formul as what listed below.
'''
for num in range(1,11): #use the circulation to print the total number for 10 times
    nums = num * (num + 1)/2 #It is the formula we learned
    print(round(nums)) #use round function to keep integer (the decimal part is zero, so use this function can just delete the decimal part)