"""
Imagine we are studying an organizational structure which consists of General Managers,
Managers, and Developers. A General Manager may have many Managers working under him
and a Manager may have many developers under him. Suppose, you have to determine the total salary of all the employees.

One of the best solutions to the above-described problem is using Composite Method by working with
a common interface that declares a method for calculating the total salary.

sp7_t5

img_3.png

Note.
We attempt to make an organizational hierarchy with sub-organization,
which may have subsequent sub-organizations, such as:
GeneralManager                                   [Composite]
      Manager1                                   [Composite]
              Developer11                        [Leaf]
              Developer12                        [Leaf]
      Manager2                                   [Composite]
              Developer21                        [Leaf]
              Developer22                        [Leaf]
"""
# https://www.geeksforgeeks.org/composite-method-python-design-patterns/

class LeafElement:
    '''Class representing objects at the bottom or Leaf of the hierarchy tree.'''

    def __init__(self, *args):
        ''''Takes the first positional argument and assigns to member variable "position".'''
        self.position = args[0]

    def showDetails(self):
        '''Prints the position of the child element.'''
        print("\t", end="")
        print(self.position)


class CompositeElement:
    '''Class representing objects at any level of the hierarchy
     tree except for the bottom or leaf level. Maintains the child
      objects by adding and removing them from the tree structure.'''

    def __init__(self, *args):
        '''Takes the first positional argument and assigns to member
         variable "position". Initializes a list of children elements.'''
        self.position = args[0]
        self.children = []

    def add(self, child):
        '''Adds the supplied child element to the list of children
         elements "children".'''
        self.children.append(child)

    def remove(self, child):
        '''Removes the supplied child element from the list of
        children elements "children".'''
        self.children.remove(child)

    def showDetails(self):
        '''Prints the details of the component element first. Then,
        iterates over each of its children, prints their details by
        calling their showDetails() method.'''
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.showDetails()


if __name__ == "__main__":
    topLevelMenu = CompositeElement("GeneralManager")
    subMenuItem1 = CompositeElement("Manager1")
    subMenuItem2 = CompositeElement("Manager2")
    subMenuItem11 = LeafElement("Developer11")
    subMenuItem12 = LeafElement("Developer12")
    subMenuItem21 = LeafElement("Developer21")
    subMenuItem22 = LeafElement("Developer22")
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem22)
    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.showDetails()