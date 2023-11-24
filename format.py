#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "<" to left-align the value:

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "<" to left-align the value:

print("\n To provide left side 20 spaces")
txt = "We have {:<20} chickens."
print(txt.format(49))

print("\n To provide right side 20 spaces")
txt = "We have {:>20} chickens."
print(txt.format(49))

print("\n To Align the text center")
txt = "We have {:^} chickens."
print(txt.format(49))

print("\n To indicate postive or negative number + or - signs")
txt = "We have {:+} chickens."
print(txt.format(49))
print(txt.format(-49))

print("\n To indicate only negative number - sign only ")
txt = "We have {:-} chickens."
print(txt.format(49))
print(txt.format(-49))


print("\n To Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers) ")
txt = "We have {:} chickens."
print(txt.format(49))
print(txt.format(-49))


print("\n Use a comma as a thousand separator")
txt = "We have {:,} chickens."
print(txt.format(5412345))

print("\n Use a underscore _  as a thousand separator")
txt = "We have {:_} chickens."
print(txt.format(5412345))

print("\n Use Binary format")
txt = "We have {:b} chickens."
print(txt.format(5412345))

print("\n Converts the value into the corresponding unicode character")
txt = "We have {:c} chickens."
print(txt.format(52))


print("\n Decimal format")
txt = "We have {:d} chickens."
print(txt.format(52))

print("\n Scientific format, with a lower case e")
txt = "We have {:e} chickens."
print(txt.format(52))

print("\n Scientific format, with a Capital case E")
txt = "We have {:E} chickens."
print(txt.format(52))

print("\n Fix point number format with decimal point")
txt = "We have {:.2f} chickens."
print(txt.format(52.12345))

print("\n Fix point number format")
txt = "We have {:2f} chickens."
print(txt.format(52.12345))

print("\n Octal format")
txt = "We have {:o} chickens."
print(txt.format(52))

print("\n Hex format, lower case")
txt = "We have {:x} chickens."
print(txt.format(52))

print("\n Hex format, upper  case")
txt = "We have {:X} chickens."
print(txt.format(52))

print("\n Number format")
txt = "We have {:n} chickens."
print(txt.format(52))

print("\n Percentage format")
txt = "We have {:%} chickens."
print(txt.format(52))





