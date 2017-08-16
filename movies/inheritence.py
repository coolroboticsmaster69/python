class Parent():
    def __init__(self,last_name,eye_color):
        print("parent constructer called")
        self.last_name=last_name
        self.eye_color=eye_color
    def show_info(self):
        print("Last name- "+self.last_name)
        print("Eye color- "+self.eye_color)



class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("Child constructer called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys=number_of_toys
    def show_info(self):
        print("Last name- "+self.last_name)
        print("Eye color- "+self.eye_color)
        print("Number of toys- "+str(self.number_of_toys))


billy_cyrus=Parent("cyrus","blue")
#billy_cyrus.show_info():
milly_cyrus=Child("cyrus","blue",5)
milly_cyrus.show_info()
