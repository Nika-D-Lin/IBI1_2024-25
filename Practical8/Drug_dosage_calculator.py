def Drug_dosage_calculator(weight, strength_of_paracetamol): #define a new function with these three parameters
    volume = 15 * weight / strength_of_paracetamol #calculate the theoretical volume
    if weight < 10 or weight > 100:
        return('Error, the weight is not in the required range.')
    else:
        if strength_of_paracetamol not in [24,50]: #compare the therotical value and input one
            return(f"Error, the strength is not in the required range.")
        else:
            return(f"Correct, the therotical value is {volume}.")
        
weight = int(input("weight:"))        
strength = int(input('chooce one from 120mg/5ml and 250mg/5ml (just input "24" or "50"):'))
print (Drug_dosage_calculator(weight,strength))

#examaple:
print(Drug_dosage_calculator(80,50))
#it will print 'Correct, the therotical value is 24.'