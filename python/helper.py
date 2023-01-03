# Please dont edit anything in this file.

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
   
   


    


list = SLinkedList()
list.headval = Node("ht")
e1 = Node("ht")
e2 = Node("tps:")
e3 = Node("//")
e4 = Node("for")
e5 = Node("tps:")
e6 = Node("ms")
e7 = Node(".")
e8 = Node("for")
e9 = Node("lumos")
e10 = Node("//")
e11 = Node("ht")
e12 = Node("labs.")
e13 = Node("ms")
e14 = Node("co")
e15 = Node("/su")
e16 = Node("rvey")
e17 = Node("for")
e18 = Node("/")
e19 = Node("labs.")
e20 = Node("t/")
e21 = Node("65a5a0c3")
e22 = Node("-15b9")
e23 = Node("-42")
e24 = Node("65a5a0c3")
e25 = Node("da")
e26 = Node("-a99c")
e27 = Node("-")
e28 = Node("06622")
e29 = Node("e0c7")
e30 = Node("bac/")
e31 = Node("r/")
e32 = Node("o")
e33 = Node("//")
e34 = Node("/su")
e35 = Node("labs.")
e36 = Node("ms")
e37 = Node("bac/")
e38 = Node("/su")
e39 = Node(".")
e40 = Node("65a5a0c3")
e41 = Node("rvey")
e42 = Node("-15b9")
e43 = Node("bac/")
e44 = Node("lumos")
e45 = Node("-42")
e46 = Node("bac/")
e47 = Node("-")
e48 = Node("bac/")
e49 = Node("rvey")
e50 = Node("r/")
e51 = Node("o")
e52 = Node(".")
e53 = Node("for")
e54 = Node("-15b9")
e55 = Node("-a99c")
e56 = Node("bac/")
e57 = Node("t/")
e58 = Node("lumos")
e59 = Node("da")
e60 = Node("da")


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

e20.nextval = e21
e21.nextval = e22
e22.nextval = e23
e23.nextval = e24
e24.nextval = e25
e25.nextval = e26
e26.nextval = e27
e27.nextval = e28
e28.nextval = e29
e29.nextval = e30
e30.nextval = e31
e31.nextval = e32
e32.nextval = e33
e33.nextval = e34
e34.nextval = e35
e35.nextval = e36
e36.nextval = e37
e37.nextval = e38
e38.nextval = e39
e39.nextval = e40
e40.nextval = e41
e41.nextval = e42
e42.nextval = e43
e43.nextval = e44
e44.nextval = e45
e45.nextval = e46
e46.nextval = e47
e47.nextval = e48
e48.nextval = e49
e49.nextval = e50
e50.nextval = e51
e51.nextval = e52
e52.nextval = e53
e53.nextval = e54
e54.nextval = e55
e55.nextval = e56
e56.nextval = e57
e57.nextval = e58
e58.nextval = e59
e59.nextval = e60


print("This is what the unsolved quest looks like: \n")
list.listprint()
print("\nPlease keep inmind that this is a linked list and we have used arrows to depict the different nodes.")
print("\n\n")

print("Hurray! I was able to solve the quest - here is my output: \n")
