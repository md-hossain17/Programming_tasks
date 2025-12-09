# main_simple.py
import svgwrite
from svgwrite import Drawing, cm, mm
from svgwrite.shapes import Rect, Circle
import os

def drawSquare(PDwg: Drawing) -> None:
    """Draw a square"""
    print("\n--- Draw Square ---")
    try:
        x = float(input("X position (mm): "))
        y = float(input("Y position (mm): "))
        size = float(input("Size (mm): "))
        color = input("Color: ").strip() or "blue"
        
        square = Rect(
            insert=(x * mm, y * mm),
            size=(size * mm, size * mm),
            fill=color
        )
        PDwg.add(square)
        print("Square added.")
    except:
        print("Invalid input.")

def drawCircle(PDwg: Drawing) -> None:
    """Draw a circle"""
    print("\n--- Draw Circle ---")
    try:
        cx = float(input("Center X (mm): "))
        cy = float(input("Center Y (mm): "))
        r = float(input("Radius (mm): "))
        color = input("Color: ").strip() or "red"
        
        circle = Circle(
            center=(cx * mm, cy * mm),
            r=r * mm,
            fill=color
        )
        PDwg.add(circle)
        print("Circle added.")
    except:
        print("Invalid input.")

def saveSvg(PDwg: Drawing) -> None:
    """Save SVG to file"""
    if not PDwg.elements:
        print("No shapes to save.")
        return
    
    filename = input("Enter filename: ").strip()
    if not filename:
        print("No filename entered.")
        return
    
    if not filename.endswith('.svg'):
        filename += '.svg'
    
    print(f"Save to {filename}? (y/n): ", end="")
    if input().strip().lower() == 'y':
        PDwg.saveas(filename, pretty=True, indent=2)
        print(f"Saved to {filename}")
    else:
        print("Save cancelled.")

def main() -> None:
    """Main program"""
    print("SVG Drawing Program")
    
    # Initialize drawing
    dwg = Drawing(size=('200mm', '200mm'))
    dwg.viewbox(width=200, height=200)
    
    while True:
        print("\n1. Draw square")
        print("2. Draw circle")
        print("3. Save svg")
        print("4. Exit")
        
        choice = input("Select: ").strip()
        
        if choice == '1':
            drawSquare(dwg)
        elif choice == '2':
            drawCircle(dwg)
        elif choice == '3':
            saveSvg(dwg)
        elif choice == '4':
            if dwg.elements:
                save = input("Save before exit? (y/n): ").strip().lower()
                if save == 'y':
                    saveSvg(dwg)
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()