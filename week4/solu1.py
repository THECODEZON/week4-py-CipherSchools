def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print('number must be int or float')
    except :
        print('unexpected error')
print(divide(10,'2'))
