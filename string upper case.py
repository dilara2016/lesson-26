class IOString():
  def __init__(self):
   self.str2 = ""
  def get_String(self):
    self.str2 = input("enter string")
  def print_String (self):
      print("result is :", self.str2.upper())
str2 = IOString()
str2.get_String()
str2.print_String()
