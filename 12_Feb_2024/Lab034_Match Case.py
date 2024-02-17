num = int(input("enter number 1-3"))

match num:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case _:
        print("no idea")
