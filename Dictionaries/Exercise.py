fname = input('Enter filepath: ')
if len(fname) < 1 : fname = 'Dictionaries\Clown.txt' # So you can hit enter to default to the clown.txt
handle = open(fname)
for lin in handle :
    lin = lin.rstrip()
    print(lin)

