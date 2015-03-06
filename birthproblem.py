""" In a country in which people only want girls
every family continues to have children until they have a girl.
If they have a boy, they have another child.
If they have a girl, they stop.
What is the proportion of boys to girls in the country?"""
import random

FAMILIES = 1000 #amount of trials.

def birth():
    """True = girl.  False = boy"""
    return random.random() > 0.5

all_children = []
for family in range(FAMILIES):
    children = []
    while True:
        child = birth()
        children.append(child)
        if child:
            break
    all_children.extend(children)

print("girls: {}, boys: {}, percentage of girls of all children: {}".format(
    all_children.count(True), all_children.count(False), all_children.count(True)/len(all_children)))
