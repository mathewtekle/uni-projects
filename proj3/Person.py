"""
File: Person.py
Date: 5/4/20
Section: 21
Email: mathewt1@umbc.edu
Description:
    Final version of the Person class used to store data regarding each member of the family
"""

class Person:

    def __init__(self, parent, child, name):
        self.parent_list = parent
        self.child = child
        self.person_name = name
        self.name_list = []

    def jsonify(self):
        return {"name": self.person_name, "children": self.child, "parents": self.parent_list}

    def print_obj(self):
        print(self.parent_list)
        print(self.child)
        print(self.person_name)

    def name(self):
        return self.person_name

    def update_parents(self, parent_name):
        if parent_name in self.parent_list:
            print("Already added as a parent.")
        else:
            self.parent_list.append(parent_name)

    def update_children(self, child_name):
        if child_name in self.child:
            print("Already added as a child.")
        else:
            self.child.append(child_name)

    def update_name(self, person_name):
        self.person_name = person_name

    def return_parent_person(self):
        return self.parent_list

    def return_child_person(self):
        return self.child

