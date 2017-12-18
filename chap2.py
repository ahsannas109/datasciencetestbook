__author__ = 'pclink'
from collections import defaultdict, Counter
#tuple test for python
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3

try:
    my_tuple[1]=3
except TypeError:
    print("tuple is immutable object")

def sum_and_product(x,y):
    return (x+y),(x*y)
s,p=sum_and_product(1,2)
# print(s)

#dictionaries in python
empty_dict = {} # Pythonic
empty_dict2 = dict() # less Pythonic
grades = { "Joel" : 80, "Tim" : 95 } # dictionary literal

try:
    allen_grade=grades["allen"]
except KeyError:
    print("KEY error that item doesnt exist in dictionary")

# if "allen" in grades:
#     print("key shouldnt exist")
# if "allen" not in grades:
#     print("key shouldnt exist correct")

joel_grades = grades.get("Joel", 0)
kates_grades = grades.get("Kate", "kch dalo to")
# print(joel_grades)
# print(kates_grades)

dd_list = defaultdict(list)
dd_list[2].append(1)
dd_list[2].append(3)
# print(dd_list)

dd_dict = defaultdict(dict)
dd_dict["hello"]["world"] = "ahsan"
# print(dd_dict)

dd_double_list = defaultdict(lambda: [0,0])
dd_double_list[2][1] = 3
dd_double_list[2][0] = 3
# print(dd_double_list)

