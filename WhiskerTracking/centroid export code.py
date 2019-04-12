import clr
clr.AddReference("System.Core")
clr.AddReference("OpenCV.Net")
clr.AddReference("Bonsai.Vision")
from System import Tuple, Math, Single, Array
import math
from System.Linq import Enumerable
from OpenCV.Net import Point, Point2f
from Bonsai.Vision import ConnectedComponentCollection

@returns(Tuple[Tuple[float,float,float,float,float,float],Tuple[float,float,float,float,float,float]])
def process(sortedRegions):
  # Order component list by decreasing area size
  #largest = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Area))
  # Order component list by centroid position
  #hSortRegionList = list(Enumerable.OrderBy(sortedRegions, lambda x:x.Centroid.X))
  vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Centroid.Y))

  if len(vSortRegionList) >=6:
    xCentroidList=Tuple.Create(float(vSortRegionList[0].Centroid.X),float(vSortRegionList[1].Centroid.X),float(vSortRegionList[2].Centroid.X),float(vSortRegionList[3].Centroid.X),float(vSortRegionList[4].Centroid.X),float(vSortRegionList[5].Centroid.X))
    yCentroidList=Tuple.Create(float(vSortRegionList[0].Centroid.Y),float(vSortRegionList[1].Centroid.Y),float(vSortRegionList[2].Centroid.Y),float(vSortRegionList[3].Centroid.Y),float(vSortRegionList[4].Centroid.Y),float(vSortRegionList[5].Centroid.Y))
  if len(vSortRegionList) ==5:
    xCentroidList=Tuple.Create(float(vSortRegionList[0].Centroid.X),float(vSortRegionList[1].Centroid.X),float(vSortRegionList[2].Centroid.X),float(vSortRegionList[3].Centroid.X),float(vSortRegionList[4].Centroid.X),float.NaN)
    yCentroidList=Tuple.Create(float(vSortRegionList[0].Centroid.Y),float(vSortRegionList[1].Centroid.Y),float(vSortRegionList[2].Centroid.Y),float(vSortRegionList[3].Centroid.Y),float(vSortRegionList[4].Centroid.Y),float.NaN)
  if len(vSortRegionList) ==4:
    xCentroidList=Tuple.Create(float(vSortRegionList[0].Centroid.X),float(vSortRegionList[1].Centroid.X),float(vSortRegionList[2].Centroid.X),float(vSortRegionList[3].Centroid.X),float.NaN,float.NaN)
    yCentroidList=Tuple.Create(float(vSortRegionList[0].Centroid.Y),float(vSortRegionList[1].Centroid.Y),float(vSortRegionList[2].Centroid.Y),float(vSortRegionList[3].Centroid.Y),float.NaN,float.NaN)
  if len(vSortRegionList) ==3:
    xCentroidList=Tuple.Create(float(vSortRegionList[0].Centroid.X),float(vSortRegionList[1].Centroid.X),float(vSortRegionList[2].Centroid.X),float.NaN,float.NaN,float.NaN)
    yCentroidList=Tuple.Create(float(vSortRegionList[0].Centroid.Y),float(vSortRegionList[1].Centroid.Y),float(vSortRegionList[2].Centroid.Y),float.NaN,float.NaN,float.NaN)
  elif len(vSortRegionList) ==2:
    xCentroidList=Tuple.Create(float(vSortRegionList[0].Centroid.X),float(vSortRegionList[1].Centroid.X),float.NaN,float.NaN,float.NaN,float.NaN)
    yCentroidList=Tuple.Create(float(vSortRegionList[0].Centroid.Y),float(vSortRegionList[1].Centroid.Y),float.NaN,float.NaN,float.NaN,float.NaN)
  elif len(vSortRegionList) == 1:
    xCentroidList=Tuple.Create(float(vSortRegionList[0].Centroid.X),float.NaN,float.NaN,float.NaN,float.NaN,float.NaN) 
    yCentroidList=Tuple.Create(float(vSortRegionList[0].Centroid.Y),float.NaN,float.NaN,float.NaN,float.NaN,float.NaN)
  else:
    xCentroidList=Tuple.Create(float.NaN,float.NaN,float.NaN,float.NaN,float.NaN,float.NaN)
    yCentroidList=Tuple.Create(float.NaN,float.NaN,float.NaN,float.NaN,float.NaN,float.NaN)

  return Tuple.Create(xCentroidList, yCentroidList)
