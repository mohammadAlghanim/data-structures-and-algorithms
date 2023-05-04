
from linked_list import Linklist
if __name__ == "__main__":
    
    Linklist1=Linklist()
    Linklist2=Linklist()
    Linklist1.insert("a")
    Linklist1.insert("b")
    Linklist1.insert("c")
    Linklist1.append("k")
    Linklist1.insert_after("a","i")
    Linklist1.insert_before("a","o")

    lista = Linklist()
    lista.append(1)
    lista.append(3)
    lista.append(6)
    # lista.append(8)
    # lista.append(11)
    # print(lista)
    listb = Linklist()
    listb.append(5)
    listb.append(9)
    listb.append(10)
    listb.append(11)
    listb.append(12)
    listb.reverse_linked_list()
    print(listb)



    # print(listb)
    list5 = Linklist()
    print(list5.zip_list(lista, listb))
    # print(list5)
    # print(Linklist1)

  

    print(Linklist1.includes("b"))
