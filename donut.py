# donut.py
import math
from typing import Tuple

def add_donut(self, basepoint: Tuple[float, float] = (0, 0), outer_diameter: int = 5, inner_diameter: int = 0, layer: str = '0'):
        """
        Adds a donut using LWPolyline with width.
        
        Parameters:
        - basepoint: Center of the donut (x, y)
        - outer_diameter: Outer diameter of the donut
        - inner_diameter: Inner hole diameter (can be 0 for a solid circle)
        - layer (str): Layer name for DXF
        """
        
        # Parameters
        inner_diameter = inner_diameter if inner_diameter < outer_diameter else 0
        const_width = outer_diameter - inner_diameter
        bulge = math.tan(math.radians(180) / 4)
        
        lwpolyline = self.msp.add_lwpolyline([], dxfattribs={"closed": True, "const_width":const_width, "layer": layer})
        
        # Points
        points = [
            (basepoint[0], basepoint[1], const_width, const_width, bulge),
            (basepoint[0] + outer_diameter, basepoint[1], const_width, const_width, bulge),
        ]
        lwpolyline.set_points(points)
        
        return lwpolyline
