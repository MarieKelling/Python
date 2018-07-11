#A09
class Shape:
 def __init__(self, no_of_sides):                           #Constructor
     self.n = no_of_sides
     self.sides = [0 for i in range(no_of_sides)]
 def inputSides(self):                                      #Propmts user input of side lengths
     self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
 def dispSides(self):                                       #Displays the length of each side
     for i in range(self.n):
         print("Side",i+1,"is",self.sides[i])
t = Shape (3)
t.inputSides()
t.dispSides()


class Triangle(Shape):
    def _init_(self):
        Shape._init_(self, 3)
    #def findArea():
        #s + s + s / 2 

t = Triangle(3)
t.inputSides()
t.dispSides()
#t.findArea() 
    
    
