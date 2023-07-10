fname = input("Enter file name: ")
fh = open(fname)
#inp = fh.read()

x=0
for x in fh:
    x = x.rstrip()
    x = x.upper()
#    x+=1
    print(x)