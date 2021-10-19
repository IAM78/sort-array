number = int(input("The number of numbers that must be entered in the array?"))


def appends(numbers):


    randomlist = []
    check = 0
    for i in range(0,numbers):


        new = float(input('your number : '))
        randomlist.append(new)


    while i < len(randomlist):
        if(randomlist[i] > randomlist[i - 1]):
           check = 1
        i += 1


    return check
if appends(number) == 1:
    


    print('yes')
else:
    print('no')