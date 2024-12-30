# Fizzbuzz
# If a number is a divisible by 3, print fizz
# If a number is a divisible by 5 , print buzz
# If a number is a divisible by both , print fizzbuzz
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)