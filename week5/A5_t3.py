def askname() -> str:
    name = input("insaert name")
    return

def greetuser(pname) -> None:
    print(f"hello{pname}")
    return

def main() -> None:
    print("program starting")
    name = askname
    greetuser(name)
    print("program ending")
    return None