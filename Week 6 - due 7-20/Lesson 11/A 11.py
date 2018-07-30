#A11
print("Program Written by Marie Kelling")

while True:

    temp = input("Input the temperature you like to convert? (e.g., 45F, 102C) : ")
    degree = temp[:-1] #Set degree to the user's inputted string minus the last character

    if temp[-1].upper() == "X":
        break;
    #Added Exception Handling
    elif degree.isdigit() != True and degree.upper() != "X":
            print("Oops! That was not a valid number. Please try again..")
            continue
    else:

        degree = int(temp[:-1]) #all of the string except for its last character
        input_type = temp[-1] #get the last character

        print("You entered: ", degree, input_type.upper())
        
        if input_type.upper() == "C":

                cToF = int(round((9 * degree) / 5 + 32))
                print("The temperature in Fahrenheit is", cToF, "degrees.")
                #Implement K
                cToK = int(round((degree + 273.15)))
                print("The temperature in Kelvin is", cToK, "degrees.")

        elif input_type.upper() == "F":

                fToC = int(round((degree - 32) * 5 / 9))
                print("The temperature in Celsius is", fToC, "degrees.")
                #Implement K
                fToK = int(round((degree - 32) * (5 / 9) + 273.15))
                print("The temperature in Kelvin is", fToK, "degrees.")

        #Added Kelvin Conversion 
        elif input_type.upper() == "K":

                kToC = int(round(degree - 273.15))
                print("The temperature in Celsius is", kToC, "degrees.")
                kToF = int(round((degree - 273.15) * 1.8 + 32))
                print("The temperature in Kelvin is", kToF, "degrees.")

        else:
          print("Input proper convention.")

print("Goodbye!")
