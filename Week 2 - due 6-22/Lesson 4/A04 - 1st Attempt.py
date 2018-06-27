print ('Assignment 04 by Matt Weisfeld')

# user input

#company = input("What is the requested car's company?")
company = "Ford"
print ("The requested company name is:" + company)
#model = input("What is the requested model?")
model = "Mustang"
print ("The requested model is:" + model)
year = input("What is the requested production year?")
print ("The requested production year is:" + year)
color = input("What is the requested color?")
print ("The requested color is:" + color)

#add code here
if company == "Ford" and model == "Mustang" and (year == "1965" or year == "1966") and color != "Yellow" :
    satisfactory = True
else:
    satisfactory = False    

if satisfactory == True:
    print ("We have the requested car in stock")
else:
    print ("Unfortunately, we do not have the requested car in stock")
