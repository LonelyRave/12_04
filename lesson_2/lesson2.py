#print('lesson_2')
# --------------
#print(1 == 1)



#print(1 == 2)


#print(738137287429)

# -------------------

#celsius = float(input("Enter temperature in degrees Celsius:"))

#farenheit = ( celsius + 32 ) * 5/9
#kelvin = celsius + 273.16

#print("Temperature in degrees Fahrenheit:", farenheit, "F")
#print("Temperature in degrees Kelvin:", kelvin, "K")
#
#-----------------------------------------------------------




#v1 = 5
#t1 = 25
#v2 = 6
#t2 = 40
#v = v1 + v2
#t = (v1*t1 + v2*t2) / v




#print("The volume of mixture:", v, "л")
#print("The temperature of mixture:" ,t, "C")

#UAH = float(input("enter amount UAH:"))
#USD = UAH * 0.027

#print("USD", USD)

#USD = float(input("enter amount USD:"))
#UAH = USD * 36.94

#print("UAH", UAH)

#UAH = float(input("enter amount UAH:"))
#EUR = UAH * 0.025




#print("EUR", EUR)

#EUR = float(input("enter amount EUR:"))
#UAH = EUR * 40.46

#print("UAH", UAH)

# -----------------------------



first_data = float(input('Enter first data'))
second_data = float(input('Enter second data'))

operation = input('Enter operation')

match operation:
    case '+':
        result = first_data + second_data
        print('Result', result)
    case '-':
        result = first_data - second_data
        print('Result', result)
    case '*':
        result = first_data * second_data
        print('Result', result)
    case '/':
        result = first_data / second_data
        print('Result', result)
    case _:
        print('Operation not vaid!')



