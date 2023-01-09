#Exception handling
#Try except else finally
while True:

    try:
        age = int(input('enter your age:  '))
        break
    except ValueError:
        print('try again')
    except:
        print('unexcepted error')

if age < 18:
     print('You can\'t play this game.')

else:
     print('You can play this game.')