even = "четное число"
odd = "нечетное число"
negative = "отрицательное "
positive = "положительное "
zero = "нулевое число"

number = int(input())

if number > 0 and (number % 2) != 0 :
    print( positive, odd)
elif number > 0 and  (number % 2) == 0 :
      print( positive, even)
elif number < 0 and  (number % 2) != 0 :  
     print( negative, odd)  
elif number < 0 and  (number % 2) == 0 :
      print( negative, even)
else:
     print(zero)      
