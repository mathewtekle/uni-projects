"""
File:    proj3.py
Author:  Mathew Teklehaimanot
Date:    5/7/2020
Section: 21
E-mail:  mathewt1@umbc.edu
Description:
  Forms a dynasty/family tree and manages the relations of the family tree members
"""

import json
from Person import Person


class DynasticDescent(Person):
    def __init__(self):
        self.load_dynasty_dict = {}
        self.add_member = ""
        self.dynasty_dict = {}
        self.parents = []
        self.children = []
        self.parent_name = ""
        self.save_complete = False
        self.parent = []
        self.child = []
        self.descendant = ""
        self.child_name = ""
        self.rule_broken = False
        self.dynasty_dict_objects = {}
        self.parent_list = []
        self.ancestors = []
        self.load_dict_objects = {}
        self.jsonified_objects = {}


    # Saving function; takes in data from JSON file
    def dynastic_load(self):
        loaded_file = input("What file do you wish to load?: ")
        temp_main_dict = {}
        temp_obj_dict = {}
        with open(loaded_file, "r") as f:
            loading_tree = json.load(f)
            loading_save_data = json.loads(loading_tree)
            #print(loading_save_data)
            temp_main_dict = loading_save_data[0]
            temp_obj_dict = loading_save_data[1]
            #print(temp_obj_dict)
            #print(temp_main_dict)
            for i in temp_obj_dict:
                for j in temp_obj_dict[i]:
                    self.dynasty_dict_objects[i] = temp_obj_dict[i][j]
                    print(temp_obj_dict[i][j])
            print(self.dynasty_dict_objects)
        load_complete = True
        if load_complete:
            print("Tree loaded. ")

    def add_members(self):
        finished_adding_family = False
        self.save_complete = False
        while finished_adding_family == False:
            self.add_member = input("What would you like to do next?: ")
            if self.add_member == "add":
                self.add_family()
            elif self.add_member == "relate":
                self.relate()
            elif self.add_member == "get parents":
                self.get_parents()
            elif self.add_member == "get grandparents":
                self.get_grandparents()
            elif self.add_member == "get ancestors":
                self.get_parents()
            elif self.add_member == "get descendants":
                self.looking_for_descendants()
            elif self.add_member == "get siblings":
                self.get_siblings()
            elif self.add_member == "save tree":
                self.save_tree()
            elif self.add_member == "quit":
                finished_adding_family = True
            elif self.add_member == "load tree":
                self.dynastic_load()

    def relate(self):
        self.parent_name = input("What is the name of the parent human?: ").upper()
        self.child_name = input("What is the name of the child human?: ").upper()
        self.update_relations()
        self.parent_list.append(self.parent_name)

    def update_relations(self):
        if self.parent_name in self.dynasty_dict.keys():
            # implement time travel paradox check fn
            # implement only two parent check fn
            self.rules_check()
            self.dynasty_dict[self.parent_name].append(self.child_name)
            # self.name_human.update_name(self.parent_name)
            current_person = self.dynasty_dict_objects[self.child_name]
            current_parent = self.dynasty_dict_objects[self.parent_name]
            current_person.update_parents(self.parent_name)
            current_person.update_children(self.child_name)
            current_parent.update_children(self.child_name)
            current_person.update_name(self.child_name)
            print("Marker for if" + str(self.dynasty_dict))
            print("Marker for parent list obj" + str(current_person.return_parent_person()))
            print("Marker for child list obj" + str(current_person.return_child_person()))
            print("Current obj" + str(current_person.name))

    def get_parents(self):
        parent_list = []
        starting_human = input("What is the name of the starting human?: ").upper()
        self.format_list(self.get_ancestors(1, parent_list, starting_human))

    def get_ancestors(self, degrees, ancestors, starting_human):
        if degrees == 0:
            ancestors.append(starting_human)
        else:
            current_person = starting_human
            parent_obj = self.dynasty_dict_objects[current_person]
            parent_of_parent = parent_obj.return_parent_person()
            for i in range(len(parent_of_parent)):
                if len(parent_of_parent) < 1:
                    print("They don't have parents")
                    return ancestors
                else:
                    current_person = parent_of_parent[i]
                    self.get_ancestors(degrees - 1, ancestors, current_person)
        return ancestors

    def add_family(self):
        human = input("What is the name of the human?: ").upper()
        self.name_human = Person([], [], human)
        self.dynasty_dict[human] = []
        self.dynasty_dict_objects[human] = self.name_human

    def get_siblings(self):
        siblings_list = []
        find_person_siblings = input("Whose siblings do you want to receive?: ")
        for i in self.dynasty_dict_objects:
            if find_person_siblings == i:
                find_siblings_obj = self.dynasty_dict_objects[i]
                search_parent_descendants = find_siblings_obj.return_parent_person()
                for z in range(len(search_parent_descendants)):
                    current_parent = search_parent_descendants[z]
                    self.format_list(self.get_descendants(1, siblings_list, current_parent, 0))
                    return siblings_list

    def looking_for_descendants(self):
        starting_descendant = input("What is the name of the human?: ").upper()
        degree_of_descent = int(input("What is the degree of descent?: "))
        descendants = []
        self.format_list(self.get_descendants(degree_of_descent, descendants, starting_descendant, 0))

    def get_descendants(self, degrees, descendants, starting_human, cnt):
        if cnt == degrees:
            descendants.append(starting_human)
        else:
            child_obj = self.dynasty_dict_objects[starting_human]
            child_of_parent = child_obj.return_child_person()
            for i in range(len(child_of_parent)):
                current_person = child_of_parent[i]
                print(current_person)
                cnt += 1
                self.get_descendants(degrees, descendants, current_person, cnt)
            return descendants

    def save_tree(self):
        save_file_name = input("What would you like to name the save file?: ")
        self.compile_objects()
        with open(save_file_name, "w") as save:
            for i in self.dynasty_dict_objects:
                person_obj = self.dynasty_dict_objects[i]
                name = person_obj.name()
                self.jsonified_objects[name] = person_obj.jsonify()
            data_saved = [self.dynasty_dict, self.jsonified_objects]
            family_json = json.dumps(data_saved)
            json.dump(family_json, save)
            self.save_complete = True
        if self.save_complete == True:
            print("Tree saved. ")

    def get_grandparents(self):
        grandparents_list = []
        starting_human = input("What is the name of the starting human?: ").upper()
        self.format_list(self.get_ancestors(2, grandparents_list, starting_human))


    def get_children(self):
        children_list = []
        starting_human = input("What is the name of the starting human?: ").upper()
        self.format_list(self.get_descendants(1, children_list, starting_human, 0))

    def get_grandchildren(self):
        grandchildren_list = []
        starting_human = input("What is the name of the starting human?: ").upper()
        self.format_list(self.get_descendants(2, grandchildren_list, starting_human, 0))

    def time_paradox_check(self):
        for i in self.dynasty_dict:
            for j in self.dynasty_dict[i]:
                if j == self.dynasty_dict[i]:
                    print("{} cannot be related to themselves".format(i))
                    self.rule_broken = True

    def too_many_parents(self):
        parent_counter = 1
        for i in self.dynasty_dict:
            if self.child_name in self.dynasty_dict[i]:
                print("parent here")
                parent_counter += 1
        if parent_counter >= 3:
            self.rule_broken = True
            
    def compile_objects(self):
        self.save_objects_dict = {}
        for i in self.dynasty_dict_objects:
            self.save_objects_dict[i] = self.dynasty_dict_objects[i]
            print(i)


    def rules_check(self):
        if self.rule_broken == False:
            self.time_paradox_check()
            self.too_many_parents()
        elif self.rule_broken == True:
            print("A family tree rule has been broken")
            self.add_members()
            self.rule_broken = False  # Make it run the program again as it'll reset the boolean variable

    def format_list(self, list_name):
        for i in list_name:
            print(i, end=" ")
        print()

if __name__ == '__main__':
    dynasty = DynasticDescent()
    finished_adding = False
    while finished_adding == False:
        dynasty.add_members()
        if dynasty.add_member == "quit":
            finished_adding = True
