# Class and Object in python


class Person:
    name = None
    age = None
    phone_no = None
    height = None
    gender = None
    profession = None

    # Methods
    def sleep(self):
        print("sleep")

    def walk(self):
        return "I am walking"


rimo_object = Person()
subh_obj = Person()

rimo_object.sleep()
