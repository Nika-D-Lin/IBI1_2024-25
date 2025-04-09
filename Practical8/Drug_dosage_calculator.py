def Drug_dosage_calculator(weight, strength_of_paracetamol): #define a new function with these three parameters
    if weight < 10 or weight > 100:
        return('Error, the weight is not in the required range.')
    else:
        if strength_of_paracetamol not in ['120mg/5ml', '250mg/5ml']: #compare the therotical value and input one
            return(f"Error, the strength is not in the required range.")
        else:
            if strength_of_paracetamol == '120mg/5ml':
                volume = 15 * weight / 24 #calculate the theoretical volume
            else:
                volume = 15 * weight / 50 #calculate the theoretical volume
            return(f"Correct, the therotical value is {volume}.")
        
weight = int(input("weight:"))        
strength = input('chooce one from 120mg/5ml and 250mg/5ml :')
print(Drug_dosage_calculator(weight,strength))

#examaple:
print(Drug_dosage_calculator(80,'250mg/5ml'))
#it will print 'Correct, the therotical value is 24.'