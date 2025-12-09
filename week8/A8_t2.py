# calculator.py

class MathOperations:
    """Library class containing arithmetic operations"""
    
    @staticmethod
    def add(PAddend1: float, PAddend2: float) -> float:
        return PAddend1 + PAddend2
    
    @staticmethod
    def subtract(PMinuend: float, PSubtrahend: float) -> float:
        return PMinuend - PSubtrahend
    
    @staticmethod
    def multiply(PMultiplicant: float, PMultiplier: float) -> float:
        return PMultiplicant * PMultiplier
    
    @staticmethod
    def divide(PDividend: float, PDivisor: float) -> float:
        if PDivisor == 0:
            raise ValueError("Division by zero is not allowed")
        return PDividend / PDivisor

def showOptions() -> None:
    print("\n" + "=" * 40)
    print("MATHEMATICAL OPERATIONS")
    print("=" * 40)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("=" * 40)

def askChoice() -> int:
    while True:
        try:
            choice = int(input("Select operation (1-5): "))
            if 1 <= choice <= 5:
                return choice
            print("Please enter 1, 2, 3, 4, or 5.")
        except ValueError:
            print("Invalid input. Enter a number.")

def askValue(PPrompt: str) -> float:
    while True:
        try:
            return float(input(PPrompt))
        except ValueError:
            print("Invalid number. Try again.")

def main() -> None:
    print("FLOATING-POINT CALCULATOR")
    print("All calculations use float precision\n")
    
    math = MathOperations()
    
    while True:
        showOptions()
        choice = askChoice()
        
        if choice == 5:
            print("\nProgram terminated.")
            break
        
        if choice == 1:
            print("\n--- ADDITION ---")
            a = askValue("First addend: ")
            b = askValue("Second addend: ")
            result = math.add(a, b)
            print(f"Result: {a} + {b} = {result}")
            
        elif choice == 2:
            print("\n--- SUBTRACTION ---")
            a = askValue("Minuend: ")
            b = askValue("Subtrahend: ")
            result = math.subtract(a, b)
            print(f"Result: {a} - {b} = {result}")
            
        elif choice == 3:
            print("\n--- MULTIPLICATION ---")
            a = askValue("Multiplicand: ")
            b = askValue("Multiplier: ")
            result = math.multiply(a, b)
            print(f"Result: {a} × {b} = {result}")
            
        elif choice == 4:
            print("\n--- DIVISION ---")
            a = askValue("Dividend: ")
            b = askValue("Divisor: ")
            try:
                result = math.divide(a, b)
                print(f"Result: {a} ÷ {b} = {result}")
            except ValueError as e:
                print(f"Error: {e}")
        
        print("\n" + "-" * 40)

if __name__ == "__main__":
    main()