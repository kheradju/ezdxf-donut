# donut.py
import math


def add_donut(msp, basepoint=(0, 0), outer_diameter=5, inner_diameter=2):
    """
    Adds a donut similar to the DONUT command in AutoCAD using LWPolyline.
    
    Parameters:
    - msp: modelspace object from your DXF document
    - basepoint: center of the donut (x, y)
    - outer_diameter: outer diameter of the donut
    - inner_diameter: inner hole diameter (if >= outer_diameter, treated as 0)

    Returns:
    - lwpolyline: created LWPolyline object
    """
    if inner_diameter >= outer_diameter:
        raise ValueError("inner_diameter must be smaller than outer_diameter.")

    outer_radius = outer_diameter
    inner_radius = inner_diameter

    # تنظیمات ضخامت
    const_width = outer_radius - inner_radius

    bulge = math.tan(math.radians(180) / 4)
    lwpolyline = msp.add_lwpolyline([], dxfattribs={"closed": True, "const_width": const_width, "layer": "0"})

    points = [
        (basepoint[0], basepoint[1], const_width, const_width, bulge),
        (basepoint[0] + outer_diameter, basepoint[1], const_width, const_width, bulge),
    ]
    lwpolyline.set_points(points)

    return lwpolyline