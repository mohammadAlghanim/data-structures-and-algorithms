
from linked_list import Linklist
if __name__ == "__main__":
    
    Linklist1=Linklist()
    Linklist1.insert("a")
    Linklist1.insert("b")
    Linklist1.insert("c")
    Linklist1.append("k")
    Linklist1.insert_after("a","i")
    Linklist1.insert_before("a","o")
    print(Linklist1)

  

    print(Linklist1.includes("b"))
