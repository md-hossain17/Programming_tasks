import os
import tempfile
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from svgwrite import Drawing
import drawlib
from drawlib import drawSquare, drawCircle, saveSvg

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

if __name__ == '__main__':
    unittest.main()