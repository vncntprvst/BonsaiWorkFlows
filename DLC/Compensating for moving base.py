## See tracking variable base issue

import clr
clr.AddReference("System.Core")
clr.AddReference("OpenCV.Net")
clr.AddReference("Bonsai.Vision")
from System import Tuple, Math, Single, Array
import math
from System.Linq import Enumerable
from OpenCV.Net import Point, Point2f
from Bonsai.Vision import ConnectedComponentCollection

base = None
NaNPoint = Point2f(float.NaN,float.NaN)
centroidLoc = NaNPoint
centroidVel = NaNPoint
distThd = 20

def FindMidPoint(inputPointArray):
    tipIdx = float(len(inputList))/2
    if tipIdx % 2 != 0:
        return (inputList[int(tipIdx - .5)])
    else:
        return (inputList[int(tipIdx)])

def FindBasePoint(inputPointArray):
  pointList = Enumerable.OrderBy(inputPointArray, lambda x:x.X)
  firstPoint = Enumerable.First(pointList)
  return firstPoint

def FindTipPoint(inputPointArray):
  pointList = Enumerable.OrderByDescending(inputPointArray, lambda x:x.X)
  lastPoint = Enumerable.First(pointList)
  return lastPoint

@returns(Point2f) 
def process(sortedRegions):
  global base, centroidLoc, centroidVel

  vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).Y))

  if len(vSortRegionList) >= 3:
    blob1Index = 2
    newbase = Point2f(FindTipPoint(vSortRegionList[blob1Index].Contour.ToArray[Point]()))
    return newbase #vSortRegionList[blob1Index].Orientation
  else:
    return NaNPoint #float(0)