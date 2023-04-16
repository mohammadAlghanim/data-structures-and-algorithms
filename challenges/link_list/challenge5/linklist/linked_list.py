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
    


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

      

    def insert_before(self, value, new_value):
       node = Node(new_value)
       if self.head == None:
        self.head = node
       else:
         current = self.head
         previous = None
         while current:
            if current.value == value:
                node.next = current
                if previous:
                    previous.next = node
                else:
                    self.head = node
                return
            previous = current
            current = current.next


    
     


    def insert_after(self,value,new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        current = self.head
        while current is not None:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                
            current = current.next
                
            
            

             
            