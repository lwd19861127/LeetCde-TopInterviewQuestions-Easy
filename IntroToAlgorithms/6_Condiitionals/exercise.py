# This is a conditional exercise.
# Write a program takes an user input for an exam mark, and prints
# the grade for that mark - according to the following scheme:
#
#
#   Mark      Grade
#   >= 90       A
#  [80-90)      B
#  [70-80)      C
#  [60-70)      D
#    < 60       F
#
#
# The square and round brackets denote closed and open intervals(range).
# A closed interval includes the number, and open interval excludes it.
# Test your program by print the mark and the grade for a number of different marks.

score = int(input("Enter your score:\n"))

if score >= 90:
    print("Your Grade is A\n")
elif score >= 80:
    print("Your Grade is B\n")
elif score >= 70:
    print("Your Grade is C\n")
elif score >= 60:
    print("Your Grade is D\n")
else:
    print("Your Grade is F\n")
