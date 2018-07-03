temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1]) #all of the string except for its last character
input_type = temp[-1] #get the last character
print("You entered: ", temp)
print("The degree entry is: ", degree)
print("The degree type is: ", input_type)

# Add code here
if temp[-1].upper() == "C":
    #Code to convert from C to F
    result = str(int(degree) * 1.8 + 32)
    output_type = "Fahrenheit"
    print("The temperature in", output_type, "is", result, "degrees.")
elif temp[-1].upper() == "F":
    #Code to convert from F to C
    result = str(int((degree) - 32) * .5556)
    output_type = "Celsius"
    print("The temperature in", output_type, "is", result, "degrees.")
else:
    print("Improper format. Please specify as Celsuis or fahrenheit")


