def Drug_dosage_calculator(weight, strength_of_paracetamol, volume): #define a new function with these three parameters
    volume0 = 15 * weight / strength_of_paracetamol #calculate the theoretical volume
    if weight < 10 or weight > 100:
        return('Error, the weight is not in the required range.')
    else:
        if volume0 != volume: #compare the therotical value and input one
            return(f"Error, the therotical value is {volume0}")
        else:
            return(f"Correct, the therotical value is {volume0}")
        
strength = int(input('chooce one from 120mg/5ml	and 250mg/5ml (just input "24" or "50"):'))
print (Drug_dosage_calculator(weight=int(input("weight:")),strength_of_paracetamol=strength, volume=input("volume:")))

#examaple:
print(Drug_dosage_calculator(weight=80,strength_of_paracetamol=strength, volume=100))
#it will print 'Error'