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
distThd = 20

def FindBasePoint(inputPointArray):
  pointList = Enumerable.OrderBy(inputPointArray, lambda x:x.Y) #For horizontal head position
  firstPoint = Enumerable.First(pointList)
  return firstPoint

def DistBetweenPoints(pt1,pt2):
  dx = abs(pt2.X - pt1.X)
  dy = abs(pt2.Y - pt1.Y)
  # distance vector
  return math.sqrt(dx**2 + dy**2)

@returns(ConnectedComponentCollection)
def process(sortedRegions):
  global noWhisker, whiskerIndex, currBase
  # Order whisker components list by base point, bottom to top
  hSortWhiskers = list(Enumerable.OrderBy(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).X))

  if noWhisker is True: #on first pass, mostly
    whiskerIndex = 1
    currBase = FindBasePoint(hSortWhiskers[whiskerIndex].Contour.ToArray[Point]())
    print("no whisker present")

  # Compare base points and find closest base, within spatial treshold limits (typically, either index 0 or 1)
  # ToDo: need to find what to do when tracked whisker has jumped to a neigboring one.  
  if len(hSortWhiskers) >= 1:
    #print("number of whisker is", len(hSortWhiskers))
    baseDist=distThd
    bestIdx=whiskerIndex
    for wIdx, wCComp in enumerate(hSortWhiskers):
      thatBase = FindBasePoint(wCComp.Contour.ToArray[Point]())
      if DistBetweenPoints(currBase, thatBase) < baseDist:
        print(wIdx, "has base distance under threshold ",  baseDist)
        baseDist = DistBetweenPoints(currBase, thatBase)
        bestIdx = wIdx 
    if baseDist < distThd:
      #print("selected base", bestIdx, "distance is below threshold: ", baseDist)
      whiskerIndex = bestIdx
      currBase = FindBasePoint(hSortWhiskers[whiskerIndex].Contour.ToArray[Point]())
    else:
      #print("selected base", bestIdx, "distance", DistBetweenPoints(currBase, thatBase), "is above threshold: ", baseDist)
      whiskerIndex = float.NaN
    noWhisker = False
  else:
    # if no whisker components, return nan
    print("no whisker component")
    noWhisker = True
    whiskerIndex = float.NaN

 
  Component = ConnectedComponentCollection(sortedRegions.ImageSize)
  if Single.IsNaN(whiskerIndex) == False:
    print("whisker",  whiskerIndex, "selected")
    Component.Add(hSortWhiskers[int(whiskerIndex)])
    
  return Component