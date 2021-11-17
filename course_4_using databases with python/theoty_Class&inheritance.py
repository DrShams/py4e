class PartyAnimal:#CLASS                                #!a template
    #dir(PartyAnimal)
        #...'name', 'party', 'x'
    x = 0#ATTRIBUTE                                     #!a variable within a class
    name = ""
    def __init__(self, z) :#CONSTRUCTOR                 #!code that runs when an object is created
        #selt under constraction instance
        #z - parameter
        #def indicate the start fo a method in PartyAnimal class
        self.name = z#where .name is the syntax to look up the name attribute
        print(self.name, "constructed")
    def party(self) :#METHOD                            #!a function within a class
        self.x = self.x + 1#where .x is the syntax to look up the value x attribute
        print(self.name,"party count",self.x)
    def __del__(self):#used rarely we could build the programm without def __del__
        #1 executes when we change variable = PartyAnimal("") to something different
        #2 executes in the end of the programm
        print('I am destructed', self.x)

class FootballFan(PartyAnimal):#INHERITANCE             #the ability to extend a class to make a new class
    #dir(FootballFan)
        #...'name', 'party', 'points', 'touchdown', 'x'
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal("Sally")#<class '__main__.PartyAnimal'>
#-> def __init__(self,z)
    #->where z can call through .name Method = "Sally"
s.party()
j = PartyAnimal("Jum")
#after reassignment def __del__(self): is not executed because we continue with PartyAnimal
j.party()
s.party()
#n = 42#-> #-> def __del__(self): ???
print("before we change s")
s = 9
#if we finished with PartyAnimal()
    #execute def __del__(self):
print("after we change s",s)
j = FootballFan("Den")
j.party()
j.touchdown()

#In Object Oriented Programming, what is another name for the "attributes" of an object?
    #fields
    #?-forms
    #?-methods
    #?-messages
    #?portions
#Which came first, the instance or the class?
    #class
    #?instance
#At the moment of creation of a new object, Python looks at the _________ definition to define the structure and capabilities of the newly created object.
    #class
    #?instance
#Which of the following is NOT a good synonym for "class" in Python?
    #direction
    #?blueprint
    #template
    #pattern
#What does this Python statement do if PartyAnimal is a class?
#zap = PartyAnimal
    #Use the PartyAnimal template to make a new object and assign it to zap
    #?Clear out all the data in the PartyAnimal variable and put the old values for the data in zap
    #?Copy the value from the PartyAnimal variable to the variable zap
#What is "self" typically used for in a Python method within a class?
    #to refer to the instance in which the method is being called
