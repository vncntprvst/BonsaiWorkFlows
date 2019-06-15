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

def FindBasePoint(inputPointArray):
  pointList = Enumerable.OrderBy(inputPointArray, lambda x:x.X)
  firstPoint = Enumerable.First(pointList)
  return firstPoint

def VDistFromLastFrame(pt1,pt2):
  #dx = (pt2.X - pt1.X)
  dy = (pt2.Y - pt1.Y)
  return dy

@returns(ConnectedComponentCollection) #(Tuple[float,float]) #ConnectedComponentCollection) #@returns(Tuple[float,int]) #@returns(Single)
def process(sortedRegions):
  global base, centroidLoc, centroidVel
  # Order blob list by descending Y base point (ie, bottom to top)
  vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).Y))

  if len(vSortRegionList) >= 1:
    blob1Index = 0
    currbase = base
    newbase = FindBasePoint(vSortRegionList[blob1Index].Contour.ToArray[Point]()) #vSortRegionList[blob1Index].Contour.ToArray[Point]()[0]
    if base is None:
      base = newbase
      #return float.NaN
    elif abs(VDistFromLastFrame(currbase, newbase)) < distThd:
      base = newbase
      #float(largest[0].Orientation)
      #return distfromlastframe(currbase, base)  
    else: # find which blob is which instead
      if len(vSortRegionList) >= blob1Index+2:
        nextbase = FindBasePoint(vSortRegionList[blob1Index+1].Contour.ToArray[Point]())
        if abs(VDistFromLastFrame(currbase, nextbase)) < distThd:
          blob1Index = blob1Index+1
          base = nextbase
        else:
          if len(vSortRegionList) >= blob1Index+3:
            nextbase = FindBasePoint(vSortRegionList[blob1Index+2].Contour.ToArray[Point]())
            if abs(VDistFromLastFrame(currbase, nextbase)) < distThd:
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

  #return Tuple.Create(blob1Index,len(leftmost))

  Component = ConnectedComponentCollection(sortedRegions.ImageSize)
  vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).Y))
  if Single.IsNaN(blob1Index) == False:
    Component.Add(vSortRegionList[int(blob1Index)])
    if int(blob1Index)+1 <= len(vSortRegionList)-1:
      Component.Add(vSortRegionList[int(blob1Index)+1])
    if int(blob1Index)+2 <= len(vSortRegionList)-1:
      Component.Add(vSortRegionList[int(blob1Index)+2])
    
  return Component