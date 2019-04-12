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
nanpoint = Point2f(float.NaN,float.NaN)
centroidLoc = nanpoint
centroidVel = nanpoint

def distfromlastframe(pt1,pt2):
  dx = (pt2.X - pt1.X)
  dy = (pt2.Y - pt1.Y)
  return dx + dy

def pointvelocity(pt1,pt2):
  dx = (pt2.X - pt1.X)
  dy = (pt2.Y - pt1.Y)
  return Point(dx,dy)

def bisector(pt1,pt2):
  dx = abs(pt2.X - pt1.X)
  dy = abs(pt2.Y - pt1.Y)
  if dx+dy !=0:
    #if abs(pt2.X) + abs(pt2.Y) < 20:
    #  return 0
    #el
    if  pt2.X <= 0:
      return (dx*dy)/math.hypot(dx, dy) #flipping polarity, as head oriented leftward
    else:
      return -(dx*dy)/math.hypot(dx, dy)
  else:
    return 0

@returns(ConnectedComponentCollection) #(Tuple[float,float]) #ConnectedComponentCollection) #@returns(Tuple[float,int]) #@returns(Single)
def process(sortedRegions):
  global base, centroidLoc, centroidVel
  # Order blob list by descending area
  #largest = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Area))
  # Order component list by rightmost centroid
  #rightmost = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Centroid.X))
  #leftmost = list(Enumerable.OrderBy(sortedRegions, lambda x:x.Centroid.X))
  bottommost = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Centroid.Y))

  if len(bottommost) >= 1:
    blob1Index = 0
    currbase = base
    newbase = bottommost[blob1Index].Contour.ToArray[Point]()[0]
    if base is None:
      base = newbase
      #return float.NaN
    elif abs(distfromlastframe(currbase, newbase)) < 20:
      base = newbase
      #float(largest[0].Orientation)
      #return distfromlastframe(currbase, base)  
    else: # find which blob is which instead
      if len(bottommost) >= blob1Index+2:
        nextbase = bottommost[blob1Index+1].Contour.ToArray[Point]()[0]
        if abs(distfromlastframe(currbase, nextbase)) < 20:
          blob1Index = blob1Index+1
          base = nextbase
        else:
          if len(bottommost) >= blob1Index+3:
            nextbase = bottommost[blob1Index+2].Contour.ToArray[Point]()[0]
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

  #return Tuple.Create(blob1Index,len(leftmost))

  Component = ConnectedComponentCollection(sortedRegions.ImageSize)
  # Order component list by bottommost centroid
  #leftmost = list(Enumerable.OrderBy(sortedRegions, lambda x:x.Centroid.X))
  bottommost = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Centroid.Y))
  if Single.IsNaN(blob1Index) == False:
    #Component.Add(bottommost[int(blob1Index)])
    if int(blob1Index)+1 <= len(bottommost)-1:
      Component.Add(bottommost[int(blob1Index)+1])
    #if int(blob1Index)+2 <= len(bottommost)-1:
      #Component.Add(bottommost[int(blob1Index)+2])
    
  return Component

  # if len(Component)>=2:
  #   currCentroid = Component[1].Centroid
  #   if Single.IsNaN(centroidLoc.X) == True: 
  #     centroidLoc=currCentroid
  #   currCentroidVel = pointvelocity(centroidLoc,currCentroid)
  #   instantVel = -bisector(centroidLoc,currCentroid)
  #   if Single.IsNaN(centroidVel.X) == True: 
  #     centroidVel=currCentroidVel
  #   instantAcc = bisector(centroidVel,currCentroidVel)
    
  #   centroidLoc = currCentroid
  #   centroidVel = currCentroidVel
  #   return Tuple.Create(float(instantAcc),float(instantVel)) #calchypot(centroidLoc,currCentroid) #currCentroidVel #centroidAcc
  # else:
  #   return Tuple.Create(float(0),float(0)) #Point(0,0) #

