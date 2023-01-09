# with open('filetext2','r') as f:
    # f.seek(len(f.read()))
    # f.write('hello \nAbout this course\n')


with open('filetext2','r') as rf:
    with open('filetext2', 'w') as wf:
        wf.write(rf.read())
