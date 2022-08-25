# FizzBuzz solved by an inline object factory.

factory = lambda y : [type('FizzBuzz', (), dict(a='FizzBuzz' if x%15==0 else 'Fizz' if x%3==0 else 'Buzz' if x%5==0 else x)).a for x in range(1, y)]
print(factory(101))