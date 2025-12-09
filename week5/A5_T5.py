def displaymenu() -> int:
    print("options: ")
    print("1- insert word")
    print("2 show current word")
    print("3- show current word in reverse")
    print("0- exit")
    return int(input("your choice:"))





def main() -> int:
    print("program starting.")
    word = ""
    choice = -1
    while choice != 0:
        choice = displaymenu()
        if choice == 1:
            word = input("insert word: ")
        elif choice == 2:
            print(f"current word is-\"{word}\"")
        elif choice == 3:
            print(f"word in reverse is-\"{word[::-1]}\"")
        elif choice == 0:
            print("exiting program") 
        else:
            print("unknown option")
    print("")
    print("program ending.")
    return None        

main()