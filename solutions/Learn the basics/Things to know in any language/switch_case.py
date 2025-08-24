"""
Link: https://takeuforward.org/plus/dsa/problems/switch-case
Name: Switch Case
Difficulty: Easy
Description:
Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.
Ensure only the 1st letter of the answer is capitalised.
For printing use:-
    for C++ : cout << variable_name;
    for Java : System.out.print();
    for Python : print()
    for Javascript : console.log()
"""

class Solution:

    # match case implementation, only works on python 3.10 or above
    # for older python versions, dictionary is recommended
    def whichWeekDay(self, day):
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
            case default:
                print("Invalid")