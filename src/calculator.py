print("Select operator")
print("+")
print("-")
print("/")
print("*")

choice = input("Select operator") 

number_1 = float(input('first number'))
number_2 = float(input('second number'))

if choice == '+':
    print(number_1 + number_2)
    
elif choice == '-':
   print(number_1 - numbber_2)
   
elif choice == '*':
    print(number_1 * number_2)
    
elif choice == '/':
    print(number_1 / number_2)

else:
    print("try again"


print('{} + {} = '.format(number_1, number_2))
print(number_1 + number_2)

print('{} * {} = ' .format(number_1, number_2))
print(number_1 * number_2)

print('{} - {} = ' .format(number_1, number_2))
print(number_1 - numbber_2)

print('{} / {} = ' .format(number_1, number_2))
print(number_1 / number_2)



