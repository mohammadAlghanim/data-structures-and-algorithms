from challenges.stack_and_queue.Queue import Queue

class AnimalShalter:
    """
    This code defines an AnimalShelter class that has two queues, one for cats and one for dogs. 
    The class has an enqueue method that takes an object representing an animal as input and enqueues it into the corresponding queue based on its species (either "cat" or "dog"). 
    The dequeue method takes a string representing the animal's species ("cat" or "dog") as input and dequeues the animal at the front of the corresponding queue. 
    If the input animal species is not "cat" or "dog", the method returns the string "null".
    In summary, this code represents a simple animal shelter system that can enqueue cats and dogs and dequeue them based on their species.
    """
    def __init__(self):
        self.cats = Queue()
        self.dog =Queue()

    def enqueue(self,obj):
        if obj["species"] == "cat":
            self.cats.enqueue(obj)
        if obj["species"] == "dog":
            self.dog.enqueue(obj)
    def dequeue(self,animal):
        if animal== "cat":
            return self.cats.dequeue()
        if animal == "dog":
            return self.dog.dequeue()
        else:
            return "null"
        
ll= AnimalShalter()

ll.enqueue({"species":"cat","name":"ddd"})
ll.enqueue({"species":"cat","name":"kkk"})
print(ll.dequeue("cat"))
        