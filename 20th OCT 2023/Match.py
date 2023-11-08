# Match - Similar to switch in java

num = int(input('Enter a num: '))

match num:
    case 1:
        print('You have entered 1')

    case 2:
        print('You have entered 2')

    case _:
        print('No idea')

##################################################
name = str(input('Enter your name: '))

match name:
    case "Rimo":
        print('Welcome Rimo')
    case "Subhasish":
        print('Welcome Subhasish')
    case _:
        print("Name not matching")


#####################################################
#
# num = int(input('Enter a num: '))
#
# match num:
#     case num>0: ---> match does not support conditions
#

