while(True):
    print("*"*50)
    print("Select Operators")
    print("*"*50)
    print("\t 1.Addition")
    print("\t 2.Subtraction")
    print("\t 3.Multiplication")
    print("\t 4.Division")
    print("\t 5.Modulo Division")
    print("\t 6.Exponentiation")
    print("\t7.Exit")
    print("*"*50)
    ch=int(input("Enter Your Choice:"))
    match(ch):
        case 1:
            print("Enter Two Values For Addition:")
            a,b=float(input("Enter First Value:")),float(input("Enter Second Value:"))
            print("\t Sum({},{})={}".format(a,b,a+b))
        case 2:
            print("Enter Two Values For Subtraction:")
            a,b = float(input("Enter First Value:")), float(input("Enter Second Value:"))
            print("\t Sub({},{})={}".format(a, b, a - b))
        case 3:
            print("Enter Two Values For Multiplication:")
            a, b = float(input("Enter First Value:")), float(input("Enter Second Value:"))
            print("\t Mul({},{})={}".format(a, b, a * b))
        case 4:
            print("Enter Two Values Division:")
            a, b = float(input("Enter First Value:")), float(input("Enter Second Value:"))
            print("\t Div({},{})={}".format(a, b, a/b))
        case 5:
            print("Enter Two Values For Modulo Division:")
            a, b = float(input("Enter First Value")), float(input("Enter Second Value"))
            print("\t Modulo Div({},{})={}".format(a, b, a%b))
        case 6:
            print("Enter Two Values For Exponention:")
            a, b = float(input("Enter First Value")), float(input("Enter Second Value"))
            print("\t Power({},{})={}".format(a, b, a**b))
        case 7:
            print("Thanks For Using This Program")
            break
        case _:
            print("Your Selection Of Operation Is Wrong ---->Try Again")



