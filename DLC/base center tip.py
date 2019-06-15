#return x,y values for base, center, tip of three central whiskers
import clr
clr.AddReference("System.Core")
clr.AddReference("OpenCV.Net")
from System import Tuple
from System.Linq import Enumerable
from OpenCV.Net import Point, Point2f

NaNPoint = Point2f(float.NaN,float.NaN)

def FindBasePoint(inputPointArray):
  pointList = Enumerable.OrderBy(inputPointArray, lambda x:x.X)
  firstPoint = Enumerable.First(pointList)
  return firstPoint

def FindTipPoint(inputPointArray):
  pointList = Enumerable.OrderByDescending(inputPointArray, lambda x:x.X)
  lastPoint = Enumerable.First(pointList)
  return lastPoint

@returns(Tuple[Tuple[Point2f,Point2f,Point2f],Tuple[Point2f,Point2f,Point2f],Tuple[Point2f,Point2f,Point2f]])
def process(sortedRegions):
  vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).Y))
  if len(vSortRegionList) >=3:
    baseList=Tuple.Create(Point2f(FindBasePoint(vSortRegionList[0].Contour.ToArray[Point]())),Point2f(FindBasePoint(vSortRegionList[1].Contour.ToArray[Point]())),Point2f(FindBasePoint(vSortRegionList[2].Contour.ToArray[Point]())))
    centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),Point2f(vSortRegionList[1].Centroid.X,vSortRegionList[1].Centroid.Y),Point2f(vSortRegionList[2].Centroid.X,vSortRegionList[2].Centroid.Y))
    tipList=Tuple.Create(Point2f(FindTipPoint(vSortRegionList[0].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[1].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[2].Contour.ToArray[Point]())))
  elif len(vSortRegionList) ==2:
    baseList=Tuple.Create(Point2f(FindBasePoint(vSortRegionList[0].Contour.ToArray[Point]())),Point2f(FindBasePoint(vSortRegionList[1].Contour.ToArray[Point]())),NaNPoint)
    centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),Point2f(vSortRegionList[1].Centroid.X,vSortRegionList[1].Centroid.Y),NaNPoint)
    tipList=Tuple.Create(Point2f(FindTipPoint(vSortRegionList[0].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[1].Contour.ToArray[Point]())),NaNPoint)
  elif len(vSortRegionList) == 1:
    baseList=Tuple.Create(Point2f(FindBasePoint(vSortRegionList[0].Contour.ToArray[Point]())),NaNPoint,NaNPoint)
    centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),NaNPoint,NaNPoint) 
    tipList=Tuple.Create(Point2f(FindTipPoint(vSortRegionList[0].Contour.ToArray[Point]())),NaNPoint,NaNPoint)
  else:
    baseList=Tuple.Create(NaNPoint,NaNPoint,NaNPoint)
    centroidList=Tuple.Create(NaNPoint,NaNPoint,NaNPoint)
    tipList=Tuple.Create(NaNPoint,NaNPoint,NaNPoint)

  return Tuple.Create(baseList, centroidList, tipList)
