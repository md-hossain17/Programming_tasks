# hexagon_demo.py
import svgwrite
import math
from svgwrite import Drawing, mm
from svgwrite.shapes import Polygon

def drawHexagon(PDwg: Drawing) -> None:
    """Draw a hexagon with exact calculation as specified"""
    print("\n=== HEXAGON CREATION ===")
    
    try:
        # Get center point
        cx = float(input("Center X (mm): "))
        cy = float(input("Center Y (mm): "))
        
        # Get apothem
        apothem = float(input("Apothem length (mm): "))
        
        if apothem <= 0:
            print("Apothem must be positive.")
            return
        
        # Calculate circumradius: R = r / cos(30°)
        circumradius = apothem / math.cos(math.radians(30))
        
        print(f"\nCalculations:")
        print(f"  Apothem (r): {apothem:.2f} mm")
        print(f"  Circumradius (R): {circumradius:.2f} mm")
        print(f"  Side length (a): {2 * apothem * math.tan(math.radians(30)):.2f} mm")
        
        # Generate points clockwise from top-right
        points = []
        print("\nCorner points (calculated):")
        
        for i in range(6):
            # Angle: 30°, 90°, 150°, 210°, 270°, 330°
            angle_deg = 30 + (i * 60)
            angle_rad = math.radians(angle_deg)
            
            # Calculate coordinates
            x = cx + circumradius * math.cos(angle_rad)
            y = cy + circumradius * math.sin(angle_rad)
            
            # Round to integers
            x_rounded = round(x)
            y_rounded = round(y)
            points.append((x_rounded, y_rounded))
            
            # Corner names
            corner_names = ["Top Right", "Right", "Bottom Right", 
                          "Bottom Left", "Left", "Top Left"]
            print(f"  {corner_names[i]}: ({x:.2f}, {y:.2f}) -> ({x_rounded}, {y_rounded})")
        
        # Get styling
        fill_color = input("\nFill color: ") or "green"
        stroke_color = input("Stroke color (Enter for none): ")
        
        # Convert points to mm
        points_mm = [(x * mm, y * mm) for x, y in points]
        
        # Create hexagon
        hexagon = Polygon(
            points=points_mm,
            fill=fill_color,
            stroke=stroke_color if stroke_color else "none"
        )
        
        PDwg.add(hexagon)
        print("✓ Hexagon added to drawing.")
        
    except ValueError:
        print("Invalid input.")

def main():
    print("Hexagon Drawing Demo")
    
    # Initialize drawing
    dwg = Drawing(size=('150mm', '150mm'))
    dwg.viewbox(width=150, height=150)
    
    # Draw example hexagon (75, 75) with apothem 60
    print("\nExample: Hexagon with center (75, 75) and apothem 60:")
    
    cx, cy = 75, 75
    apothem = 60
    
    # Calculate circumradius
    circumradius = apothem / math.cos(math.radians(30))
    
    # Calculate points
    points = []
    for i in range(6):
        angle_deg = 30 + (i * 60)
        angle_rad = math.radians(angle_deg)
        x = cx + circumradius * math.cos(angle_rad)
        y = cy + circumradius * math.sin(angle_rad)
        points.append((round(x), round(y)))
    
    print("Points:", points)
    
    # Draw user hexagon
    drawHexagon(dwg)
    
    # Save
    if dwg.elements:
        dwg.saveas("hexagon.svg", pretty=True, indent=2)
        print("\nSaved to hexagon.svg")

if __name__ == "__main__":
    main()