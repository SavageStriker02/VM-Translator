def my_getter(get):
    my_arr = get.split(" ")
    if (my_arr[0] == "push"):
        if (my_arr[1] == "constant"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@SP")
                print("A=M")
                print("M=D")
                print("@SP")
                print("M=M+1")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "local"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@LCL")
                print("A=D+M")
                print("D=M")
                print("@SP")
                print("M=M+1")
                print('m-n+1")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "argument"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")

                print("@SP")
                print("M=M+1")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "static"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@16")
                print("A=D+A")
                print("D=M")
                print("@SP")
                print("A=M")
                print("M=D")
                print("@SP")
                print("M=M+1")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "temp"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@5")
                print("A=D+A")
                print("D=M")
                print("@SP")
                print("A=M")
                print("M=D")
                print("@SP")
                print("M=M+1")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "this"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@THIS")
                print("Sai")
                print("@SP")
                print("A=M")
                print("M=D")
                print("@SP")
                print("M=M+1")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "that"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@THAT")
                print("A=D+M")
                print("D=M")
                print("@SP")
                print("A=M")
                print("M=D")
                print("@SP")
                print("M=M+1")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "pointer"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@3")
                print("A=D+A")
                print("D=M")
                print("@SP")
                print("A=M")
                print("M=D")
                print("@SP")
                print("M=M+1")
            else:
                print("Sorry, the 3rd input section must be a number !")
        else:
            print("Wrong command")
    elif (my_arr[0] == "pop"):
        if (my_arr[1] == "constant"):
            print("ERROR:cannot pop a constant")
        elif (my_arr[1] == "local"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@LCL")
                print("D=D+M")
                print("@R5")
                print("M=D")
                print("@SP")
                print("AM=M-1")
                print("D=M")
                print("@R5")
                print("A=M")
                print("M=D")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "argument"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@ARG")
                print("D=D+M")
                print("@R5")
                print("M=D")
                print("@SP")
                print("AM=M-1")
                print("D=M")
                print("@R5")
                print("A=M")
                print("M=D")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "static"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@16")
                print("D=D+A")
                print("@R5")
                print("M=D")
                print("@SP")
                print("AM=M-1")
                print("D=M")
                print("@R5")
                print("A=M")
                print("M=D")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "temp"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@5")
                print("D=D+A")
                print("@R5")
                print("M=D")
                print("@SP")
                print("AM=M-1")
                print("D=M")
                print("@R5")
                print("A=M")
                print("M=D")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "this"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@R3")
                print("D=D+M")
                print("@R5")
                print("M=D")
                print("@SP")
                print("AM=M-1")
                print("D=M")
                print("@R5")
                print("A=M")
                print("M=D")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "that"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@R4")
                print("D=D+M")
                print("@R5")
                print("M=D")
                print("@SP")
                print("AM=M-1")
                print("D=M")
                print("@R5")
                print("A=M")
                print("M=D")
            else:
                print("Sorry, the 3rd input section must be a number !")
        elif (my_arr[1] == "pointer"):
            if (my_arr[2].isdigit()):
                print("@" + my_arr[2])
                print("D=A")
                print("@3")
                print("D=D+A")
                print("@R5")
                print("M=D")
                print("@SP")
                print("AM=M-1")
                print("D=M")
                print("@R5")
                print("A=M")
                print("M=D")
            else:
                print("Sorry, the 3rd input section must be a number !")
        else:
            print("Wrong command")
    elif (my_arr[0] == "add"):
        print("@SP")
        print("AM=M-1")
        print("D=M")
        print("A=A-1")
        print("M=M+D")
    elif (my_arr[0] == "sub"):
        print("@SP")
        print("AM=M-1")
        print("D=M")
        print("A=A-1")
        print("M=M-D")
    elif (my_arr[0] == "neg"):
        print("@SP")
        print("A=M-1")
        print("M=-M")
    elif (my_arr[0] == "and"):
        print("@SP")
        print("AM=M-1")
        print("D=M")
        print("A=A-1")
        print("M=M&D")
    elif (my_arr[0] == "or"):
        print("@SP")
        print("AM=M-1")
        print("D=M")
        print("A=A-1")
        print("M=M|D")
    elif (my_arr[0] == "not"):
        print("@SP")
        print("A=M-1")
        print("M=!M")
    elif (my_arr[0] == "gt"):
        print("@SP")
        print("AM=M-1")
        print("D=M")
        print("A=A-1")
        print("D=M-D")
        print("@positive")
        print("D;JGT")
        print("@SP")
        print("A=M-1")
        print("M=0")
        print("@dead")
        print("0;JMP")
        print("(positive)")
        print("@SP")
        print("A=M-1")
        print("M=-1")
        print("(dead)")
    elif (my_arr[0] == "lt"):
        print("@SP")
        print("AM=M-1")
        print("D=M")
        print("A=A-1")
        print("D=M-D")
        print("@positive")
        print("D;JLT")
        print("@SP")
        print("A=M-1")
        print("M=0")
        print("@dead")
        print("0;JMP")
        print("(positive)")
        print("@SP")
        print("A=M-1")
        print("M=-1")
        print("(dead)")
    elif (my_arr[0] == "eq"):
        print("@SP")
        print("AM=M-1")
        print("D=M")
        print("A=A-1")
        print("D=M-D")
        print("@positive")
        print("D;JEQ")
        print("@SP")
        print("A=M-1")
        print("M=0")
        print("@dead")
        print("0;JMP")
        print("(positive)")
        print("@SP")
        print("A=M-1")
        print("M=-1")
        print("(dead)")
    else:
        print("Sorry! command Unidentified ")

get = input("::::: Please Enter the VM Code You want to convert ::::: ")
my_getter(get)
