import clr
clr.AddReference("System.Core")
clr.AddReference("OpenCV.Net")
from System import Tuple
from System.Linq import Enumerable
from OpenCV.Net import Point, Point2f

NaNPoint = Point2f(float.NaN,float.NaN)

@returns(Tuple[Tuple[Point2f,Point2f,Point2f,Point2f,Point2f,Point2f],Tuple[Point2f,Point2f,Point2f,Point2f,Point2f,Point2f]])
def process(sortedRegions):
  # Order component list by decreasing area size
  #largest = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Area))
  # Order component list by centroid position
  hSortRegionList = list(Enumerable.OrderBy(sortedRegions, lambda x:x.Centroid.X))
  #vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Centroid.Y))
  if len(hSortRegionList) >=6:
    baseList=Tuple.Create(Point2f(hSortRegionList[0].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[1].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[2].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[3].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[4].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[5].Contour.ToArray[Point]()[0]))
    centroidList=Tuple.Create(Point2f(hSortRegionList[0].Centroid.X,hSortRegionList[0].Centroid.Y),Point2f(hSortRegionList[1].Centroid.X,hSortRegionList[1].Centroid.Y),Point2f(hSortRegionList[2].Centroid.X,hSortRegionList[2].Centroid.Y),Point2f(hSortRegionList[3].Centroid.X,hSortRegionList[3].Centroid.Y),Point2f(hSortRegionList[4].Centroid.X,hSortRegionList[4].Centroid.Y),Point2f(hSortRegionList[5].Centroid.X,hSortRegionList[5].Centroid.Y))
  if len(hSortRegionList) ==5:
    baseList=Tuple.Create(Point2f(hSortRegionList[0].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[1].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[2].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[3].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[4].Contour.ToArray[Point]()[0]),NaNPoint)
    centroidList=Tuple.Create(Point2f(hSortRegionList[0].Centroid.X,hSortRegionList[0].Centroid.Y),Point2f(hSortRegionList[1].Centroid.X,hSortRegionList[1].Centroid.Y),Point2f(hSortRegionList[2].Centroid.X,hSortRegionList[2].Centroid.Y),Point2f(hSortRegionList[3].Centroid.X,hSortRegionList[3].Centroid.Y),Point2f(hSortRegionList[4].Centroid.X,hSortRegionList[4].Centroid.Y),NaNPoint)
  if len(hSortRegionList) ==4:
    baseList=Tuple.Create(Point2f(hSortRegionList[0].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[1].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[2].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[3].Contour.ToArray[Point]()[0]),NaNPoint,NaNPoint)
    centroidList=Tuple.Create(Point2f(hSortRegionList[0].Centroid.X,hSortRegionList[0].Centroid.Y),Point2f(hSortRegionList[1].Centroid.X,hSortRegionList[1].Centroid.Y),Point2f(hSortRegionList[2].Centroid.X,hSortRegionList[2].Centroid.Y),Point2f(hSortRegionList[3].Centroid.X,hSortRegionList[3].Centroid.Y),NaNPoint,NaNPoint)
  if len(hSortRegionList) ==3:
    baseList=Tuple.Create(Point2f(hSortRegionList[0].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[1].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[2].Contour.ToArray[Point]()[0]),NaNPoint,NaNPoint,NaNPoint)
    centroidList=Tuple.Create(Point2f(hSortRegionList[0].Centroid.X,hSortRegionList[0].Centroid.Y),Point2f(hSortRegionList[1].Centroid.X,hSortRegionList[1].Centroid.Y),Point2f(hSortRegionList[2].Centroid.X,hSortRegionList[2].Centroid.Y),NaNPoint,NaNPoint,NaNPoint)
  elif len(hSortRegionList) ==2:
    baseList=Tuple.Create(Point2f(hSortRegionList[0].Contour.ToArray[Point]()[0]),Point2f(hSortRegionList[1].Contour.ToArray[Point]()[0]),NaNPoint,NaNPoint,NaNPoint,NaNPoint)
    centroidList=Tuple.Create(Point2f(hSortRegionList[0].Centroid.X,hSortRegionList[0].Centroid.Y),Point2f(hSortRegionList[1].Centroid.X,hSortRegionList[1].Centroid.Y),NaNPoint,NaNPoint,NaNPoint,NaNPoint)
  elif len(hSortRegionList) == 1:
    baseList=Tuple.Create(Point2f(hSortRegionList[0].Contour.ToArray[Point]()[0]),NaNPoint,NaNPoint,NaNPoint,NaNPoint,NaNPoint)
    centroidList=Tuple.Create(Point2f(hSortRegionList[0].Centroid.X,hSortRegionList[0].Centroid.Y),NaNPoint,NaNPoint,NaNPoint,NaNPoint,NaNPoint) 
  else:
    baseList=Tuple.Create(NaNPoint,NaNPoint,NaNPoint,NaNPoint,NaNPoint,NaNPoint)
    centroidList=Tuple.Create(NaNPoint,NaNPoint,NaNPoint,NaNPoint,NaNPoint,NaNPoint)

  return Tuple.Create(baseList, centroidList)
