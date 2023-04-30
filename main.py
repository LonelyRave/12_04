# print('lesson_2')
# --------------
# print(1 == 1)

# print(1 == 2)


# print(738137287429)

# -------------------

# celsius = float(input("Enter temperature in degrees Celsius:"))

# farenheit = ( celsius + 32 ) * 5/9
# kelvin = celsius + 273.16

# print("Temperature in degrees Fahrenheit:", farenheit, "F")
# print("Temperature in degrees Kelvin:", kelvin, "K")
#
# -----------------------------------------------------------

# №2 ПЕРЕЗДАЧА
 v1 = float(input('Set v1:'))
 t1 = float(input('Set t1:'))
 v2 = float(input('Set v2:'))
 t2 = float(input('Set t2:'))
 v = v1 + v2
 t = (v1*t1 + v2*t2) / (v1 + v2)

 print("The volume of mixture:", v, "L")
 print("The temperature of mixture:", t, "C")

# UAH = float(input("enter amount UAH:"))
# USD = UAH * 0.027

# print("USD", USD)

# USD = float(input("enter amount USD:"))
# UAH = USD * 36.94

# print("UAH", UAH)

# UAH = float(input("enter amount UAH:"))
# EUR = UAH * 0.025


# print("EUR", EUR)

# EUR = float(input("enter amount EUR:"))
# UAH = EUR * 40.46

# print("UAH", UAH)

# -----------------------------
# №3 ПЕРЕЗДАЧА
exchange_operation = float(input("Choose exchange operation by number:\n1.UAH --> USD \n2.USD --> UAH\n3.UAH --> EUR \n4.EUR --> UAH\n"))
amount = float (input ( 'Enter amount :'))
USD = 36.94
EUR = 40

if exchange_operation == 1:
    print (amount/36.94)
if exchange_operation == 2:
    print(amount * 36.94)
if exchange_operation == 3:
    print(amount / 40)
if exchange_operation == 4:
    print(amount * 40)
else:
    print(USD)













# first_data = float(input('Enter first data'))
# second_data = float(input('Enter second data'))
#
# operation = input('Enter operation')
#
# match operation:
#     case '+':
#         result = first_data + second_data
#         print('Result', result)
#     case '-':
#         result = first_data - second_data
#         print('Result', result)
#     case '*':
#         result = first_data * second_data
#         print('Result', result)
#     case '/':
#         result = first_data / second_data
#         print('Result', result)
#     case _:
#         print('Operation not vaid!')
