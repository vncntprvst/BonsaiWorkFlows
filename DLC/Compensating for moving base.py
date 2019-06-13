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

def SmallestX(inputPointArray):
  pointList = Enumerable.OrderBy(inputPointArray, lambda x:x.X)
  firstPoint = Enumerable.First(pointList)
  return firstPoint

def LargestX(inputPointArray):
  pointList = Enumerable.OrderByDescending(inputPointArray, lambda x:x.X)
  lastPoint = Enumerable.First(pointList)
  return lastPoint

#def distfromlastframe(pt1,pt2):
#  dx = (pt2.X - pt1.X)
#  dy = (pt2.Y - pt1.Y)
#  return dx + dy

def Vdistfromlastframe(pt1,pt2):
  #dx = (pt2.X - pt1.X)
  dy = (pt2.Y - pt1.Y)
  return dy

@returns(Point2f) #(float) #(ConnectedComponentCollection) #(Tuple[float,float]) #ConnectedComponentCollection) #@returns(Tuple[float,int]) #@returns(Single)
def process(sortedRegions):
  global base, centroidLoc, centroidVel
  # Order blob list by descending area
  #leftmost = list(Enumerable.OrderBy(sortedRegions, lambda x:x.Centroid.X))
  vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Centroid.Y))

  if len(vSortRegionList) >= 3:
    blob1Index = 2
    #if vSortRegionList[blob1Index].Orientation<0: #base and tip inverted
    #  newbase = Point2f(FindMidPoint(vSortRegionList[blob1Index].Contour.ToArray[Point]()))
    #else:
    #  newbase = Point2f(vSortRegionList[blob1Index].Contour.ToArray[Point]()[0])
    newbase = Point2f(LargestX(vSortRegionList[blob1Index].Contour.ToArray[Point]()))
    return newbase #vSortRegionList[blob1Index].Orientation
  else:
    return NaNPoint #float(0)


  # if len(vSortRegionList) >= 1:
  #   blob1Index = 0
  #   currbase = base
  #   newbase = vSortRegionList[blob1Index].Contour.ToArray[Point]()[0]
  #   if base is None:
  #     base = newbase
  #     #return float.NaN
  #   elif abs(Vdistfromlastframe(currbase, newbase)) < distThd:
  #     base = newbase
  #     #float(largest[0].Orientation)
  #     #return distfromlastframe(currbase, base)  
  #   else: # find which blob is which instead
  #     if len(vSortRegionList) >= blob1Index+2:
  #       nextbase = vSortRegionList[blob1Index+1].Contour.ToArray[Point]()[0]
  #       if abs(Vdistfromlastframe(currbase, nextbase)) < distThd:
  #         blob1Index = blob1Index+1
  #         base = nextbase
  #       else:
  #         if len(vSortRegionList) >= blob1Index+3:
  #           nextbase = vSortRegionList[blob1Index+2].Contour.ToArray[Point]()[0]
  #           if abs(Vdistfromlastframe(currbase, nextbase)) < distThd:
  #             blob1Index = blob1Index+2
  #             base = nextbase
  #           else: #keep previous value
  #             blob1Index = float.NaN
  #             base = base
  #         else:
  #           blob1Index = float.NaN
  #     else:
  #       blob1Index = float.NaN
  #     #return distfromlastframe(currbase, base)  
  #   blob1Index = float(blob1Index)
  # else:
  #   # otherwise, return nan
  #   base = None
  #   blob1Index = float.NaN

  # #return Tuple.Create(blob1Index,len(leftmost))

  # Component = ConnectedComponentCollection(sortedRegions.ImageSize)
  # # Order component list by vSortRegionList centroid
  # #leftmost = list(Enumerable.OrderBy(sortedRegions, lambda x:x.Centroid.X))
  # vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Centroid.Y))
  # if Single.IsNaN(blob1Index) == False:
  #   Component.Add(vSortRegionList[int(blob1Index)])
  #   if int(blob1Index)+1 <= len(vSortRegionList)-1:
  #     Component.Add(vSortRegionList[int(blob1Index)+1])
  #   if int(blob1Index)+2 <= len(vSortRegionList)-1:
  #     Component.Add(vSortRegionList[int(blob1Index)+2])
    
  # return Component
