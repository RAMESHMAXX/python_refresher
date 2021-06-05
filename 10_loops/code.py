val=input("to play game 'y'for yes and 'n' for not to play: ")
magic_no=100
x=True
while(x):
    if(val=="y" or val=="Y"):
        no=int(input("enter number for winning game: "))
        if(magic_no==no):
            print("you are winner!! ")
        else:
            print("difference by: ",no-magic_no," losses game!")
        break       #goto outside of loop
    else:
        print("you are not plaing game ok!! ")
        break


#--now for loop
for i in range(10):
    print(i)
        