import clr
clr.AddReference("System.Core")
clr.AddReference("OpenCV.Net")
clr.AddReference("Bonsai.Vision")
from System import Tuple, Math, Single, Array
import math
from System.Linq import Enumerable
from OpenCV.Net import Point, Point2f
from Bonsai.Vision import ConnectedComponentCollection

noWhisker = True
NaNPoint = Point2f(float.NaN,float.NaN)
baseDistThd = 20
centroidDistThd = 100

def FindBasePoint(inputPointArray):
  pointList = Enumerable.OrderBy(inputPointArray, lambda x:x.Y) #Y point for horizontal head position
  firstPoint = Enumerable.First(pointList)
  return firstPoint

def DistBetweenPoints(pt1,pt2):
  dx = abs(pt2.X - pt1.X)
  dy = abs(pt2.Y - pt1.Y)
  # distance vector
  return math.sqrt(dx**2 + dy**2)

@returns(ConnectedComponentCollection)
def process(sortedRegions):
  global noWhisker, whiskerIndex, currBase, currCentroid
  # Order whisker components list by base point, bottom to top
  #vSortWhiskers = list(Enumerable.OrderByDescending(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).Y))
  hSortWhiskers = list(Enumerable.OrderBy(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).X))

  if noWhisker is True: #on first pass, mostly
    whiskerIndex = 1
    currBase = FindBasePoint(hSortWhiskers[whiskerIndex].Contour.ToArray[Point]())
    currCentroid = hSortWhiskers[whiskerIndex].Centroid
    #print("init")

  # Compare base points and find closest base, within spatial treshold limits (typically, either index 0 or 1)
  # ToDo: need to find what to do when tracked whisker has jumped to a neigboring one.  
  if len(hSortWhiskers) >= 1:
    baseDist=baseDistThd
    centroidDist=centroidDistThd
    bestIdx=whiskerIndex
    for wIdx, wCComp in enumerate(hSortWhiskers):
      thatBase = FindBasePoint(wCComp.Contour.ToArray[Point]())
      #print(DistBetweenPoints(currCentroid, thatCentroid))
      #print(DistBetweenPoints(currBase, thatBase))
      if DistBetweenPoints(currBase, thatBase) < baseDist: #check if centroid is also compatible
        thatCentroid = wCComp.Centroid
        #print(DistBetweenPoints(currBase, thatBase))
        if DistBetweenPoints(currCentroid, thatCentroid) < centroidDist:
          print("distance between centroids", DistBetweenPoints(currCentroid, thatCentroid))
          centroidDist = DistBetweenPoints(currCentroid, thatCentroid)
          baseDist = DistBetweenPoints(currBase, thatBase)
          bestIdx = wIdx
        else:
          print("Centroids too far: ", DistBetweenPoints(currCentroid, thatCentroid))
    if baseDist < baseDistThd:
      whiskerIndex = bestIdx
      currBase = FindBasePoint(hSortWhiskers[whiskerIndex].Contour.ToArray[Point]())
      currCentroid = hSortWhiskers[whiskerIndex].Centroid
    else:
      whiskerIndex = float.NaN
    noWhisker = False
  else:
    # if no whisker components, return nan
    noWhisker = True
    whiskerIndex = float.NaN

 
  Component = ConnectedComponentCollection(sortedRegions.ImageSize)
  if Single.IsNaN(whiskerIndex) == False:
    Component.Add(hSortWhiskers[int(whiskerIndex)])
    
  return Component