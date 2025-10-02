def other(input):
    '''You are in the other function'''
    #The input is neither Yes or No
    print("\nInvalid input, sorry")

def abort(input):
    '''You are in the abort function'''
    if input == "No" or input == "N" or input == "n" or input == "no":
        print("\nAbort Shutting Down")
    else:
        other(input)

def shutting_down(input):
    '''You are in the shutting_down function'''
    if input == "Yes" or input == "Y" or input ==  "y" or input == "yes":
        print("\nShutting Down")
    else:
        abort(input)

answer = str(input("Enter if you want to shut down or abort (Yes/No): "))
shutting_down(answer)

if answer == "Yes" or answer == "Y" or answer == "y" or answer == "yes":
    print(shutting_down.__doc__)
elif answer == "No" or answer == "N" or answer == "n" or answer == "no":
    print(abort.__doc__)
else:
    print(other.__doc__)