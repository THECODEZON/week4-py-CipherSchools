with open ('index.html','r') as webpage:
    with open('index.html', 'a') as wf:
        page = webpage.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos == -1:
            else :
                first_quote = page.find('\"',pos)
                second_quote = page.find('\"',first_quote+1)
                url = page[first_quote+1:second_quote]
                wf.write(url + '\n')
