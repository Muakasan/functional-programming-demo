from functools import *
from itertools import *

class Robot:
    def __init__(self, size, color, metal_type):
        self.size = size
        self.color = color
        self.metal_type = metal_type
    def __str__(self):
        return "{0}, {1}, {2}".format(self.size, self.color, self.metal_type)
    def __repr__(self):
        return "Robot({0}, {1}, {2})".format(self.size, self.color, self.metal_type)

some_robots = \
[Robot(11, "Red", "Bronze"), Robot(3, "Yellow", "Bronze"), Robot(20, "Red", "Titanium"), \
Robot(50, "Yellow", "Silver"), Robot(11, "Red", "Bronze"), Robot(100, "Yellow", "Silver"),
Robot(40, "Green", "Bronze"), Robot(5, "Green", "Titanium"), Robot(11, "Green", "Bronze")]

some_fruits = ["apple", "banana", "raspberry", "banana", "apple", "banana", "pineapple", "raspberry"]

def build_robots(tuples):
    return []

def red_or_yellow(fruits):
    def r_or_y(fruit):
        return "Red"
    return []

def only_red_robots(robots):
    return []

def robot_greater_ten(robot):
    return True

def only_robots_greater_ten(robots):
    return []

def average_robot_size(robots):
    return 0

def my_filter(some_list, some_func):
    return []

def main():
    print("Build Robots:", build_robots([(10, "Green", "Silver"), (45, "Purple", "Titanium"), (2, "Red", "Aluminum")]))
    print("Red or Yellow:", red_or_yellow(some_fruits))
    print("Only Red Robots:", only_red_robots(some_robots))
    print("Only Robots Greater than Size 10:", only_robots_greater_ten(some_robots))
    print("Average Robot Size:", average_robot_size(some_robots))
    print("My Filter:", my_filter(some_robots, robot_greater_ten))

if __name__ == '__main__':
    main()