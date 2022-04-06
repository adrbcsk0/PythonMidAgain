options = ['Option1', 'Option2', 'Option3']
txt=""

while not txt:
    txt = input('Dawaj opcję:1, 2, 3?', )
else:
    try:
        int(txt)
        #print(type(txt))
    except:
        print('to nie liczba')


if txt == '1':
    print(options[0])
elif txt == '2':
    print(options[1])
elif txt == '3':
    print(options[2])
else:
    print('Zły wybór, brak opcji')
