try:
    a = 10
    print(a)
    raise NameError("Hello")
except NameError as e:
    print("An exception occurred")
    print(e)

try:
    a=10/0;
    print ("Exception occurred" )
finally:
    print ("Code to be executed" )