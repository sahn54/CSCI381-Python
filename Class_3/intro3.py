# Problem:
# Re-write the following if statement so that it is syntactically correct; then figure out what will be
# printed. Test your answer by running the reformatted code.
# x = 9
# y = 8
# z = 7
# if x > 9: if y > 8: print ("x > 9 and y > 8") else: if z >= 7: print("x <= 9 and z >= 7") else: print("x <= 9 and z < 7")
# In many programming languages the general rule regarding” nested” if statements (an if in the
# block of another if) is that the “else” goes with the closest “if” that has no “else.”
# Answer:

# recursion

x = 9
y = 8
z = 7

# Second Form
# if x > 9:
#     if y > 8:
#         print("x > 9 and y > 8")
#     else:
#         if z >= 7:
#             print("x <= 9 and z >= 7")
# else:
#     print("x <= 9 and z < 7")

# Third Form
if x <= 9:
    print("x <= 9 and z < 7")
elif y <= 8:
    print("x > 9 and y > 8")
elif z >= 7:
    print("x <= 9 and z >= 7")
