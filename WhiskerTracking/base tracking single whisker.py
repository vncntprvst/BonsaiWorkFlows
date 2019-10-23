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
  pointList = Enumerable.OrderBy(inputPointArray, lambda x:x.X)
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
  vSortWhiskers = list(Enumerable.OrderByDescending(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).Y))

  if noWhisker is True: #on first pass, mostly
    whiskerIndex = 0
    currBase = FindBasePoint(vSortWhiskers[whiskerIndex].Contour.ToArray[Point]())
    #print("init")

  # Compare base points and find closest base, within spatial treshold limits (typically, either index 0 or 1)
  # ToDo: need to find what to do when tracked whisker has jumped to a neigboring one.  
  if len(vSortWhiskers) >= 1:
    baseDist=distThd
    bestIdx=whiskerIndex
    for wIdx, wCComp in enumerate(vSortWhiskers):
      thatBase = FindBasePoint(wCComp.Contour.ToArray[Point]())
      if DistBetweenPoints(currBase, thatBase) < baseDist:
        baseDist = DistBetweenPoints(currBase, thatBase)
        bestIdx = wIdx 
    if baseDist < distThd:
      whiskerIndex = bestIdx
      currBase = FindBasePoint(vSortWhiskers[whiskerIndex].Contour.ToArray[Point]())
    else:
      whiskerIndex = float.NaN
    noWhisker = False
  else:
    # if no whisker components, return nan
    noWhisker = True
    whiskerIndex = float.NaN

 
  Component = ConnectedComponentCollection(sortedRegions.ImageSize)
  if Single.IsNaN(whiskerIndex) == False:
    Component.Add(vSortWhiskers[int(whiskerIndex)])
    
  return Component