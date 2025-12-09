def none():
    return None
def frameword(pword) -> none:
    print("*"*(len(pword)+4))
    print(f"* '{pword} '*")
    print("*")
    return none

def main():
    print("program starting")
    word =str(input("insert word: "))
    frameword(word)
    print("")
    print("program ending")
    return none

main()
