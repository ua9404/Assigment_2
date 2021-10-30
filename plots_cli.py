


def quit(y, n):
    input("are you sure (y/n): ")
    if input == y:
        print(True)
    elif input == n:
        print(False)

quit(y="true", n="false")
print("Goodbye!")


input("Enter a command or 'quit' to quit: ")
try:
    if input == 'quit':
     quit(y="goodbye", n="Continue")
     print("Goodbye!")
    else:
        print("Goodbye!")
except:
    print("Invalid command")
    print("Please try again")



