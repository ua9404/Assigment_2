import csv
import plotter


def quit(y, n,):
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
    if input == 'stu':
        print("Continue")
except:
    print("Invalid command")
    print("Please try again")

def student_average(stu):
    try:
     input = open(excel_file.csv)
    if input == stu:
        print("plot finished (window maybe hidden")
    else:
        print("plot failed (no such student)")
        input.close()
    except:
    print("usage: stu <filename> <firstname> <lastname>")
    print("no such file")


def print_average(a_string):
    return True
print("average grade: ")
