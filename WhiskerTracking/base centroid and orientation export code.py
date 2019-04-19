import clr
clr.AddReference("System.Core")
clr.AddReference("OpenCV.Net")
from System import Tuple
from System.Linq import Enumerable
from OpenCV.Net import Point, Point2f

NaNPoint = Point2f(float.NaN,float.NaN)

@returns(Tuple[Tuple[Point2f,Point2f,Point2f,Point2f,Point2f,Point2f],
  Tuple[Point2f,Point2f,Point2f,Point2f,Point2f,Point2f]])


## Maximum number of elements in Tuple is 7 - no adding orientation then. 


def process(sortedRegions):
  # Order component list by decreasing area size
  #largest = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Area))
  # Order component list by centroid position
  #hSortRegionList = list(Enumerable.OrderBy(sortedRegions, lambda x:x.Centroid.X))
  vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Centroid.Y))
  if len(vSortRegionList) >=6:
    baseList=Tuple.Create(Point2f(vSortRegionList[0].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[1].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[2].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[3].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[4].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[5].Contour.ToArray[Point]()[0]))
    centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),
      Point2f(vSortRegionList[1].Centroid.X,vSortRegionList[1].Centroid.Y),
      Point2f(vSortRegionList[2].Centroid.X,vSortRegionList[2].Centroid.Y),
      Point2f(vSortRegionList[3].Centroid.X,vSortRegionList[3].Centroid.Y),
      Point2f(vSortRegionList[4].Centroid.X,vSortRegionList[4].Centroid.Y),
      Point2f(vSortRegionList[5].Centroid.X,vSortRegionList[5].Centroid.Y))
  elif len(vSortRegionList) ==5:
    baseList=Tuple.Create(Point2f(vSortRegionList[0].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[1].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[2].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[3].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[4].Contour.ToArray[Point]()[0]),NaNPoint)
    centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),
      Point2f(vSortRegionList[1].Centroid.X,vSortRegionList[1].Centroid.Y),
      Point2f(vSortRegionList[2].Centroid.X,vSortRegionList[2].Centroid.Y),
      Point2f(vSortRegionList[3].Centroid.X,vSortRegionList[3].Centroid.Y),
      Point2f(vSortRegionList[4].Centroid.X,vSortRegionList[4].Centroid.Y),NaNPoint)
  elif len(vSortRegionList) ==4:
    baseList=Tuple.Create(Point2f(vSortRegionList[0].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[1].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[2].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[3].Contour.ToArray[Point]()[0]),NaNPoint,NaNPoint)
    centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),
      Point2f(vSortRegionList[1].Centroid.X,vSortRegionList[1].Centroid.Y),
      Point2f(vSortRegionList[2].Centroid.X,vSortRegionList[2].Centroid.Y),
      Point2f(vSortRegionList[3].Centroid.X,vSortRegionList[3].Centroid.Y),NaNPoint,NaNPoint)
  elif len(vSortRegionList) ==3:
    baseList=Tuple.Create(Point2f(vSortRegionList[0].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[1].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[2].Contour.ToArray[Point]()[0]),NaNPoint,NaNPoint,NaNPoint)
    centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),
      Point2f(vSortRegionList[1].Centroid.X,vSortRegionList[1].Centroid.Y),
      Point2f(vSortRegionList[2].Centroid.X,vSortRegionList[2].Centroid.Y),NaNPoint,NaNPoint,NaNPoint)
  elif len(vSortRegionList) ==2:
    baseList=Tuple.Create(Point2f(vSortRegionList[0].Contour.ToArray[Point]()[0]),
      Point2f(vSortRegionList[1].Contour.ToArray[Point]()[0]),NaNPoint,NaNPoint,NaNPoint,NaNPoint)
    centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),
      Point2f(vSortRegionList[1].Centroid.X,vSortRegionList[1].Centroid.Y),NaNPoint,NaNPoint,NaNPoint,NaNPoint)
  elif len(vSortRegionList) == 1:
    baseList=Tuple.Create(Point2f(vSortRegionList[0].Contour.ToArray[Point]()[0]),
      NaNPoint,NaNPoint,NaNPoint,NaNPoint,NaNPoint)
    centroidList=Tuple.Create(Point2f(vSortRegionList[0].Centroid.X,vSortRegionList[0].Centroid.Y),
      NaNPoint,NaNPoint,NaNPoint,NaNPoint,NaNPoint) 
  else:
    baseList=Tuple.Create(NaNPoint,NaNPoint,NaNPoint,NaNPoint,NaNPoint,NaNPoint)
    centroidList=Tuple.Create(NaNPoint,NaNPoint,NaNPoint,NaNPoint,NaNPoint,NaNPoint)

  return Tuple.Create(baseList, centroidList)
