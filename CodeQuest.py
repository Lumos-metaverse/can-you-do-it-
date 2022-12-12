# Welcome to the Lumos Coding Quest 
# at line 25 you will find the "MyAnswer()" function 
# that is the only function you need to edit and add your answer
# you have been given a linkedlist. this linkedlist contains a jumbled link. upon removing the duplicate nodes systematically, and compiling the string distributed inside the linkedlist you will find the link and will be allowed to whitelist yourself for the lumos metaverse.
# please note that apart from line 25 you are not editing any other line
# Make sure that you tag @LumoslabsHQ and tweet about your journey as you fight this quest and emerge victorious

class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      answer = ""
      while printval is not None:
         answer += printval.dataval
         printval = printval.nextval
      print (answer)
   
   def MyAnswer(self):
    #write your answer here
    answer=''


    


list = SLinkedList()
list.headval = Node("ht")
e1 = Node("ht")
e2 = Node("tps:")
e3 = Node("//")
e4 = Node("//")
e5 = Node("bit")
e6 = Node(".")
e7 = Node("bit")
e8 = Node("ht")
e9 = Node(".")
e10 = Node("ly")
e11 = Node("/")
e12 = Node("Lumos")
e13 = Node("Whitelist")
e14 = Node("Whitelist")
e15 = Node("Lumos")
e16 = Node("ht")
e17 = Node("tps:")
e18 = Node("Lumos")
e19 = Node("ly")
e20 = Node("Lumos")

# Link first Node to second node
list.headval.nextval = e1

# Link second Node to third node
e1.nextval = e2
# Link third Node to fourth node
e2.nextval = e3
e3.nextval = e4
# Link fourth Node to fifth node
e4.nextval = e5
# Link fifth Node to sixth node
e5.nextval = e6
# Link sixth Node to seventh node
e6.nextval = e7
e7.nextval = e8
e8.nextval = e9
e9.nextval = e10
e10.nextval = e11
e11.nextval = e12
e12.nextval = e13
e13.nextval = e14
e14.nextval = e15
e15.nextval = e16
e16.nextval = e17
e17.nextval = e18
e18.nextval = e19
e19.nextval = e20

print("This is what the unsolved quest looks like: \n")
list.listprint()
print("\n\n")

print("Hurray! I was able to solve the quest - here is my output \n")
list.MyAnswer()

