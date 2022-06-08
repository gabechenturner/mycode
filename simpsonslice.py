#!/usr/bin/env python3
"""Morning Slicing Challenge!"""

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

def main():
    """write your code in this function to solve the challenge"""

    # write one print function for each list above
    # get the strings "eyes," "goggles," and "nothing from each
    # final output for each print should look like this:
    """My eyes! The goggles do nothing!"""

    print(f"My {challenge [2][1]}! the {challenge [2][0]} do {challenge [3]}!")
    print(f"MY {trial [2][1]}! the {trial [2][0]} do {trial [3]!")
    # print()

if __name__ == "__main__": # <-- what is this??? we will review later :)
    main()
