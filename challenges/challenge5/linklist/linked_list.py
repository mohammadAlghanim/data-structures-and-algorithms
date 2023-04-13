class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def insert(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next =self.head
            self.head =newNode

    def includes(self,key):
        temp= self.head
        while temp is not None:
            if temp.value == key:
                return True
            temp = temp.next
        if temp is None:
            return False
        
    def __str__(self):
        output = ""
        
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} -->'
                current = current.next
            
            output += " None"
        return output
    

            
                
            
            

             
            