num = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    # '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'zero'
}


phone = input("Phone: ")
output = ""
for i in phone:
    output += num.get(i, "!") + " "
print(output)
# print(num[i], end=" ")
