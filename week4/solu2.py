with open ('solution', 'r') as rf:
    with open('sol2','a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f'{name}\'s salary is {salary} ')