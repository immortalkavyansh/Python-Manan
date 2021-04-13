# Creating a class
class Student:
    Free_Leaves = 8
    pass
#Class
Manan = Student()
Harry = Student()
#Manan
Manan.name = "Manan"
Manan.school = "Choithram"
Manan.std = 7
Manan.subjects = ["Maths", "Computer Science"]

#Harry
Harry.name = "Harry"
Harry.school = "Choithram"
Harry.std = 6
Harry.subjects = ["comerse", "buisness studies"]
# print(Manan.school, Manan.name, Manan.std)
# print(Harry.school, Harry.std, Harry.name)

# oops 2
print(Manan.__dict__) #Dict = Dictionary
print(Harry.__dict__)

Manan.Free_Leaves = 10#Will chanege the value of variable personal
print(Manan.__dict__)


