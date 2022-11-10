# calculator #
num1 = input("Enter first number : ")
num2 = input("Enter second number : ")
first = float(num1)
second = float(num2)
print("----press keys for operator (+,-,*,/,%,//,** )----------")
operator = input("Enter operator : ")

if operator == "+":
   print("The sum is : ",first + second)
elif operator == "-":
   print("The subtraction is : ",first - second)
elif operator == "*":
   print("The multiplication is : ",first * second)
elif operator == "**":
   print("The powered value is : ",first ** second)# powered value
elif operator == "/":
   print("The divide is : ",first / second)
elif operator == "//":
   print("The floor value is : ",first // second)# floored value
elif operator == "%":
   print("The reminder is : ",first % second)
else:
   print("Invalid Operation")



