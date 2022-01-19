from numpy import w

f = open("myfile.txt", "r")
f1 = f.readlines()
for x in f1:
    print(x)
f.close()
f2 = open('myfilecopy.txt',w+)

