"""
File:    proj3_test.py
Author:  Mathew Teklehaimanot
Date:    5/4/2020
Section: 21
E-mail:  mathewt1@umbc.edu
Description:
  Tests proj3 class
"""
from wip_proj3 import DynasticDescent
from Person import Person

class dynasticTest(DynasticDescent, Person):

    DynasticDescent.dynasty_list = {"Bob": "George", "George": {"John": "Jackson"}, "John": {"Jackson": "Jack"},
                                    "Jack": {"Drew": "Matt"}}

    def test_get_parents(self):
        if "Bob" in DynasticDescent.dynasty_list:
            return True
        if "John" in DynasticDescent.dynasty_list:
            return True
        if "George" in DynasticDescent.dynasty_list:
            return True
        if "Matt" in DynasticDescent.dynasty_list:
            return True
        if "Drew" in DynasticDescent.dynasty_list:
            return True
        for i in DynasticDescent.dynasty_list:
            if "Jack" in DynasticDescent.dynasty_list[i]:
                return False

    def test_get_children(self):
        if "John" in DynasticDescent.dynasty_list:
            return True
        if "Jackson" in DynasticDescent.dynasty_list:
            return True
        if "Jack" in DynasticDescent.dynasty_list:
            return True
        if "Bob" in DynasticDescent.dynasty_list:
            return False

    def test_add_members(self):
        DynasticDescent.parent_name = "Drew"
        DynasticDescent.add_family()
        if DynasticDescent.parent_name in DynasticDescent.parents:
            return True

        DynasticDescent.parent_name = "Saz"
        DynasticDescent.add_family()
        if DynasticDescent.parent_name in DynasticDescent.parents:
            return True

        DynasticDescent.parent_name = "Klein"
        DynasticDescent.add_family()
        if DynasticDescent.parent_name in DynasticDescent.parents:
            return True

        DynasticDescent.parent_name = "Calvin"
        DynasticDescent.add_family()
        if DynasticDescent.parent_name in DynasticDescent.parents:
            return True

        DynasticDescent.parent_name = "Ryan"
        DynasticDescent.add_family()
        if DynasticDescent.parent_name in DynasticDescent.parents:
            return True

        DynasticDescent.parent_name = "Bravo"
        DynasticDescent.add_family()
        if DynasticDescent.parent_name in DynasticDescent.parents:
            return True

        DynasticDescent.parent_name = "JohnnyBoy"
        DynasticDescent.add_family()
        if DynasticDescent.parent_name in DynasticDescent.parents:
            return True

        DynasticDescent.parent_name = "OmegaLUL"
        DynasticDescent.add_members()
        if DynasticDescent.parent_name in DynasticDescent.parents:
            return False

        DynasticDescent.parent_name = "Logan"
        DynasticDescent.add_members()
        if DynasticDescent.parent_name not in DynasticDescent.parents:
            return True



    def test_save_tree(self):
        DynasticDescent.save_tree()
        if DynasticDescent.save_complete == True:
            return True
        else:
            return False




if __name__ == '__main__':
    dynasty = DynasticDescent()
