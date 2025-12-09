"""
drawLib.py - SVG Drawing Library
Implements functions to draw shapes and save SVG files.
"""

from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle
import os

def drawSquare(PDwg: Drawing, left: float, top: float, sideLength: float, 
               color: str = 'none', strokeColor: str = 'black') -> None:
    """
    Draw a square (rectangle with equal sides) and add it to the drawing.
    
    Args:
        PDwg: SVG Drawing object
        left: X position in coordinate units
        top: Y position in coordinate units
        sideLength: Length of each side in coordinate units
        color: Fill color (default: 'none')
        strokeColor: Stroke color (default: 'black')
    """
    # Create a square (rectangle with equal width and height)
    square = Rect(
        insert=(left, top),
        size=(sideLength, sideLength),
        fill=color,
        stroke=strokeColor,
        stroke_width=1  # Default stroke width
    )
    
    PDwg.add(square)
    return None

def drawCircle(PDwg: Drawing, centerX: float, centerY: float, radius: float,
               color: str = 'none', stroke: str = 'black') -> None:
    """
    Draw a circle and add it to the drawing.
    
    Args:
        PDwg: SVG Drawing object
        centerX: X coordinate of center
        centerY: Y coordinate of center
        radius: Circle radius in coordinate units
        color: Fill color (default: 'none')
        stroke: Stroke color (default: 'black')
    """
    # Create a circle
    circle = Circle(
        center=(centerX, centerY),
        r=radius,
        fill=color,
        stroke=stroke,
        stroke_width=1  # Default stroke width
    )
    
    PDwg.add(circle)
    return None

def saveSvg(PDwg: Drawing, filename: str) -> None:
    """
    Save the SVG drawing to a file.
    
    Args:
        PDwg: SVG Drawing object
        filename: Name of the file to save
        
    Raises:
        ValueError: If filename is empty
        PermissionError: If cannot write to file
    """
    if not filename:
        raise ValueError("Filename cannot be empty")
    
    # Ensure .svg extension
    if not filename.lower().endswith('.svg'):
        filename += '.svg'
    
    try:
        # Save with pretty formatting (2-space indentation)
        PDwg.saveas(
            filename,
            pretty=True,
            indent=2
        )
    except Exception as e:
        raise IOError(f"Failed to save SVG: {e}")
    
    return None

# The test code (should be in a separate file, but including here for clarity)
if __name__ == "__main__":
    import tempfile
    import unittest
    
    class TestSvgDrawing(unittest.TestCase):
        def setUp(self):
            self.dwg = Drawing()

        def test_draw_square(self):
            drawSquare(self.dwg, left=10, top=10, sideLength=100, color='red', strokeColor='black')
            shapes = list(self.dwg.elements)
            self.assertTrue(any(elem.__class__.__name__ == 'Rect' for elem in shapes))

        def test_draw_circle(self):
            drawCircle(self.dwg, centerX=50, centerY=50, radius=25, color='blue', stroke='gray')
            shapes = list(self.dwg.elements)
            self.assertTrue(any(elem.__class__.__name__ == 'Circle' for elem in shapes))

        def test_save_svg(self):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.svg') as temp_file:
                temp_filename = temp_file.name

            try:
                drawSquare(self.dwg, left=0, top=0, sideLength=50, color='green', strokeColor='black')
                saveSvg(self.dwg, temp_filename)
                self.assertTrue(os.path.exists(temp_filename))
                with open(temp_filename, 'r') as f:
                    content = f.read()
                    self.assertIn('<svg', content)
            finally:
                os.remove(temp_filename)

    # Run the tests
    unittest.main(argv=[''], exit=False)