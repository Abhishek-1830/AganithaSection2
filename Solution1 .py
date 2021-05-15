# -*- coding: utf-8 -*-
"""Solution1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qxz76RDt8A4UpXyy_hhVVShfY2HyhWwM
"""

class X:
  count = 0
  objectMap = {}
  def __init__(self, name):
    self.name = name
  
  def init(self, name):
    self.name = name
    print(self.name)
    X.objectMap[name] = self

  def execute(self, args):
    print("Arguments: ", args)
    print("Object name: ", self.name)
    X.count = X.count + 1

  def shutdown(self):
    print(self.name)
    del X.objectMap[self.name]

class A(X):
  count = 0
  def __init__(self, name):
    super().init(name)
  
  def init(self, name):
    super().init(name)
    print("Class name: A")
    
  def execute(self, args):
    print(args)
    super().execute(args)
    print("Class name: A")
    A.count = A.count + 1

  def shutdown(self):
    super().shutdown()
    print("Class name: A")
    del self

class B(X):
  count = 0
  def __init__(self, name):
    super().init(name)
  
  def init(self, name):
    super().init(name)
    print("Class name: B")
    
  def execute(self, args):
    super().execute(args)
    print("Class name: B")
    B.count = B.count + 1

  def shutdown(self):
    super().shutdown()
    print("Class name: B")
    del self

class C(X):
  count = 0
  def __init__(self, name):
    super().init(name)
  
  def init(self, name):
    super().init(name)
    print("Class name: C")
    
  def execute(self, args):
    super().execute(args)
    print("Class name: C")
    C.count = C.count + 1

  def shutdown(self):
    super().shutdown()
    print("Class name: C")
    del self

def main():
  print("Hello and Welcome to this Interactive Program!!!")
  print("There are 3 operations, namely: 'a', 'b' and 'c'")
  print("Let's go! Input one of the operation:(Enter 'a', 'b' or 'c')")

  operation = input("Enter 'a', 'b' or 'c':('q' to quit)")

  while(operation != 'q'):
    if(operation == 'a'):
      classToCreate = input("Enter what class of object you want to create:(Input 'A', 'B' or 'C')")
      nameOfObject = input("Enter the name you want to give to the object")
      if(classToCreate == 'A'):
        newObject = A(nameOfObject)
      elif(classToCreate == 'B'):
        newObject = B(nameOfObject)
      elif(classToCreate == 'C'):
        newObject = C(nameOfObject)
      else:
        print("Invalid input of class name")
    elif(operation == 'b'):
      objectToDelete = input("Enter the name of the object you want to delete")
      if(objectToDelete in X.objectMap.keys()):
        X.objectMap[objectToDelete].shutdown()
      else:
        print("The object of given name doesn't exist")
    elif(operation == 'c'):
      objectToExecute = input("Enter the name of the object to execute")
      args = input("Enter the arguments:")
      if(objectToExecute in X.objectMap.keys()):
        X.objectMap[objectToExecute].execute(args)
      else:
        print("The object of given name doesn't exist")
    else:
      print("Invalid input")
    print("Want to continue?")
    operation = input("Enter 'a', 'b' or 'c':('q' to quit)")

  print("Your Usage statistics:")
  print("Your total executions count: ", X.count)
  print("Executions of A: ", A.count)
  print("Executions of B: ", B.count)
  print("Executions of C: ", C.count)
  print("Thanks for your inputs!!!")

if __name__ == "__main__":
  main()

