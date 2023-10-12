lowerlimit = int(input('enter the lower range limit: '))
upperlimit = int(input('enter the higher range limit: '))
divisiblenumber = int(input('enter the number to be divided by'))
for i in range(lowerlimit,upperlimit):
    if i%divisiblenumber == 0:
        print(i)