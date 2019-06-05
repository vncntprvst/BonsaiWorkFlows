#return x,y values for base, center, tip of three central whiskers
import clr
clr.AddReference("System.Core")
clr.AddReference("OpenCV.Net")
from System import Tuple
from System.Linq import Enumerable
from OpenCV.Net import Point, Point2f

NaNPoint = Point2f(float.NaN,float.NaN)

def FindTipPoint(inputList):
    tipIdx = float(len(inputList))/2
    if tipIdx % 2 != 0:
        return (inputList[int(tipIdx - .5)])
    else:
        return (inputList[int(tipIdx)])

# @returns(Tuple[Tuple[Point2f,Point2f,Point2f,Point2f,Point2f,Point2f],Tuple[Point2f,Point2f,Point2f,Point2f,Point2f,Point2f],Tuple[Point2f,Point2f,Point2f,Point2f,Point2f,Point2f]])
@returns(Tuple[Tuple[Point2f,Point2f,Point2f],Tuple[Point2f,Point2f,Point2f],Tuple[Point2f,Point2f,Point2f]])
def process(sortedRegions):
  vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Centroid.Y))
  # if len(vSortRegionList) >=6:
  #   baseList=Tuple.Create(Point2f(vSortRegionList[0].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[1].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[2].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[3].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[4].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[5].Contour.ToArray[Point]()[0]))
  #   centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),Point2f(vSortRegionList[1].Centroid.X,vSortRegionList[1].Centroid.Y),Point2f(vSortRegionList[2].Centroid.X,vSortRegionList[2].Centroid.Y),Point2f(vSortRegionList[3].Centroid.X,vSortRegionList[3].Centroid.Y),Point2f(vSortRegionList[4].Centroid.X,vSortRegionList[4].Centroid.Y),Point2f(vSortRegionList[5].Centroid.X,vSortRegionList[5].Centroid.Y))
  #   tipList=Tuple.Create(Point2f(FindTipPoint(vSortRegionList[0].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[1].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[2].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[3].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[4].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[5].Contour.ToArray[Point]())))
  # elif len(vSortRegionList) ==5:
  #   baseList=Tuple.Create(Point2f(vSortRegionList[0].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[1].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[2].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[3].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[4].Contour.ToArray[Point]()[0]),NaNPoint)
  #   centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),Point2f(vSortRegionList[1].Centroid.X,vSortRegionList[1].Centroid.Y),Point2f(vSortRegionList[2].Centroid.X,vSortRegionList[2].Centroid.Y),Point2f(vSortRegionList[3].Centroid.X,vSortRegionList[3].Centroid.Y),Point2f(vSortRegionList[4].Centroid.X,vSortRegionList[4].Centroid.Y),NaNPoint)
  #   tipList=Tuple.Create(Point2f(FindTipPoint(vSortRegionList[0].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[1].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[2].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[3].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[4].Contour.ToArray[Point]())),NaNPoint)
  # elif len(vSortRegionList) ==4:
  #   baseList=Tuple.Create(Point2f(vSortRegionList[0].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[1].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[2].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[3].Contour.ToArray[Point]()[0]),NaNPoint,NaNPoint)
  #   centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),Point2f(vSortRegionList[1].Centroid.X,vSortRegionList[1].Centroid.Y),Point2f(vSortRegionList[2].Centroid.X,vSortRegionList[2].Centroid.Y),Point2f(vSortRegionList[3].Centroid.X,vSortRegionList[3].Centroid.Y),NaNPoint,NaNPoint)
  #   tipList=Tuple.Create(Point2f(FindTipPoint(vSortRegionList[0].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[1].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[2].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[3].Contour.ToArray[Point]())),NaNPoint,NaNPoint)
  # el
  if len(vSortRegionList) >=3:
    baseList=Tuple.Create(Point2f(vSortRegionList[0].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[1].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[2].Contour.ToArray[Point]()[0]))
    centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),Point2f(vSortRegionList[1].Centroid.X,vSortRegionList[1].Centroid.Y),Point2f(vSortRegionList[2].Centroid.X,vSortRegionList[2].Centroid.Y))
    tipList=Tuple.Create(Point2f(FindTipPoint(vSortRegionList[0].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[1].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[2].Contour.ToArray[Point]())))
  elif len(vSortRegionList) ==2:
    baseList=Tuple.Create(Point2f(vSortRegionList[0].Contour.ToArray[Point]()[0]),Point2f(vSortRegionList[1].Contour.ToArray[Point]()[0]),NaNPoint)
    centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),Point2f(vSortRegionList[1].Centroid.X,vSortRegionList[1].Centroid.Y),NaNPoint)
    tipList=Tuple.Create(Point2f(FindTipPoint(vSortRegionList[0].Contour.ToArray[Point]())),Point2f(FindTipPoint(vSortRegionList[1].Contour.ToArray[Point]())),NaNPoint)
  elif len(vSortRegionList) == 1:
    baseList=Tuple.Create(Point2f(vSortRegionList[0].Contour.ToArray[Point]()[0]),NaNPoint,NaNPoint)
    centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),NaNPoint,NaNPoint) 
    tipList=Tuple.Create(Point2f(FindTipPoint(vSortRegionList[0].Contour.ToArray[Point]())),NaNPoint,NaNPoint)
  else:
    baseList=Tuple.Create(NaNPoint,NaNPoint,NaNPoint)
    centroidList=Tuple.Create(NaNPoint,NaNPoint,NaNPoint)
    tipList=Tuple.Create(NaNPoint,NaNPoint,NaNPoint)

  return Tuple.Create(baseList, centroidList, tipList)
