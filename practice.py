from tempfile import TemporaryFile


print("Hello world")



a = 10
b = 0
c = 5

try:
    print(a/b)
except ZeroDivisionError:
    print("Cannot be divisible by 0")