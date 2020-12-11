import math

Pi = math.pi
def cone_area (r, h):
    try:
        Area = (Pi*r)*(r+math.sqrt(h**2+r**2))
        Area = round(Area, 4)
        return Area

    except (TypeError, UnboundLocalError, ValueError):
        print("Error not a number")
        return ""


 