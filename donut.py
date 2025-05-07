# donut.py
import math


def add_donut(self, basepoint=(0, 0), outer_diameter=5, inner_diameter=0, layer=0):
    """
        Adds a donut (filled circle with thickness) using LWPolyline with width.
        
        Parameters:
        - basepoint: Center of the donut (x, y)
        - outer_diameter: Outer diameter of the donut
        - inner_diameter: Inner hole diameter (can be 0 for a solid circle)
        - layer (str): Layer name for DXF
        """
        outer_radius = outer_diameter
        inner_radius = inner_diameter if inner_diameter < outer_diameter else 0

        const_width = outer_radius - inner_radius
        
        bulge = math.tan(math.radians(180) / 4)
        lwpolyline = self.msp.add_lwpolyline([], dxfattribs={"closed": True, "const_width":const_width, "layer": layer})
        points = [
            (basepoint[0], basepoint[1], const_width, const_width, bulge),
            (basepoint[0] + outer_diameter, basepoint[1], const_width, const_width, bulge),
        ]
        lwpolyline.set_points(points)
        
        return lwpolyline
