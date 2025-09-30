def other(input):
    '''You are in the other function'''
    #The input is neither Yes or No
    print("\nSorry")

def abort(input):
    '''You are in the abort function'''
    if input == "No" or "N" or "n" or "no":
        print("\nAbort Shutting Down")
    else:
        other(input)

def shutting_down(input):
    '''You are in the shutting_down function'''
    if input == "Yes" or "Y" or "y" or "yes":
        print("\nShutting Down")
    else:
        abort(input)

answer = str(input("Enter if you want to shut down or abort (Yes/No): "))
shutting_down(answer)

if answer == "Yes" or "Y" or "y" or "yes":
    print(shutting_down.__doc__)
elif answer == "No" or "N" or "n" or "no":
    print(abort.__doc__)
else:
    print(other.__doc__)