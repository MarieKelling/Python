#A 13 - Marie Kelling 

class Node :
    def __init__( self, data ) :
        self.data = data
        self.next = None
        self.prev = None

class LinkedList :
    def __init__( self ) :
        self.head = None        

    def add( self, data ) :
        node = Node( data )
        if self.head == None :  
            self.head = node
        else :
            node.next = self.head
            node.next.prev = node                       
            self.head = node

    def remove(self, p):                
                temp = p.prev
                p.prev.next = p.next
                p.prev = temp 
                
                
    def search( self, k ) :
        p = self.head
        if p != None :
            while p.next != None :
                if ( p.data == k ) :
                    return p                
                p = p.next
            if ( p.data == k ) :
                return p
        return None 

    def __str__( self ) :
        s = ""
        p = self.head
        if p != None :      
            while p.next != None :
                s += p.data
                p = p.next
            s += p.data
        return s

# example code
l = LinkedList()

print ("Add: a")
l.add ('a')
print ("List = ", l, "\n")

print ("Add: b")
l.add ('b')
print ("List = ", l, "\n")

print ("Add: c")
l.add ('c')
print ("List = ", l, "\n")

#Delete node b
#print ("Search: b")
p = l.search('b')
#print ("The searched Node's data = " + p.data)
#print()
print ("Remove: b")
l.remove(p)
print ("List = ", l, "\n")
