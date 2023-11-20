# use of sign (<) and (>)
# code to find the max temperatur of a day in week
monday=int(input("Enter temperature"))
tuesday=int(input("Enter temperature"))
wednesday=int(input("Enter temperature"))
thursday=int(input("Enter temperature"))
friday=int(input("Enter temperature"))
saturday=int(input("Enter temperature"))
sunday=int(input("Enter temperature"))
max=monday
if tuesday>max:
    max=tuesday
if wednesday>max:
    max=wednesday
if thursday>max:
    max=thursday
if friday>max:
    max=friday
if saturday>max:
    max=saturday
if sunday>max:
    max=sunday
print(max)