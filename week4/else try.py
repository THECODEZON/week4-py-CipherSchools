#else and try

while True:
    try:
        number = int(input('enter number: '))
        print(f'user input = {number}')
        break
    except ValueError:
        print("please type integer !! s")
    except:
        print('unexpected error !!!')
    else:
        print(f'user input = {number}')
        break

    finally:
        print('finally block.....................')