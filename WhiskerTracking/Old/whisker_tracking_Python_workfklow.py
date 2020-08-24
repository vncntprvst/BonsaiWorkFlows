import clr
clr.AddReference("System.Core")
clr.AddReference("OpenCV.Net")
from System import Tuple, Math, Single, Array
from System.Linq import Enumerable
from OpenCV.Net import Point, Point2f

base = None
#tip = None

def distfromlastframe(pt1,pt2):
  dx = (pt2.X - pt1.X)
  dy = (pt2.Y - pt1.Y)
  return dx + dy

@returns(Tuple[float,int]) #@returns(Single)
def process(value):
  global base
  # Order blob list by descending area
  #largest = list(Enumerable.OrderByDescending(value, lambda x:x.Area))
  # Order component list by rightmost centroid
  rightmost = list(Enumerable.OrderByDescending(value, lambda x:x.Centroid.X))

  if len(rightmost) >= 1:
    blob1Index = 0
    currbase = base
    newbase = max(rightmost[blob1Index].Contour.ToArray[Point]())
    if base is None:
      base = newbase
      #return float.NaN
    elif abs(distfromlastframe(currbase, newbase)) < 20:
      base = newbase
      #float(largest[0].Orientation)
      #return distfromlastframe(currbase, base)  
    else: # find which blob is which instead
      if len(rightmost) >= blob1Index+2:
        nextbase = max(rightmost[blob1Index+1].Contour.ToArray[Point]())
        if abs(distfromlastframe(currbase, nextbase)) < 20:
          blob1Index = blob1Index+1
          base = nextbase
        else:
          if len(rightmost) >= blob1Index+3:
            nextbase = max(rightmost[blob1Index+2].Contour.ToArray[Point]())
            if abs(distfromlastframe(currbase, nextbase)) < 20:
              blob1Index = blob1Index+2
              base = nextbase
            else: #keep previous value
              blob1Index = float.NaN
              base = base
          else:
            blob1Index = float.NaN
      else:
        blob1Index = float.NaN
      #return distfromlastframe(currbase, base)  
    blob1Index = float(blob1Index)
  else:
    # otherwise, return nan
    base = None
    blob1Index = float.NaN

  return Tuple.Create(blob1Index,len(rightmost))