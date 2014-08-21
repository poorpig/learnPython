def displayNumType(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!'
displayNumType(-69)
displayNumType(1.0)
displayNumType(9999999999999999999)
displayNumType(5.2+2.9j)
displayNumType('xxx')
#continueFlag = True
#while continueFlag:
#    input_num = raw_input('Enter a num:')
#    if (input_num == 'end'):
#        print 'DONE!'
#        continueFlag = False
#    else:
#        displayNumType(input_num)