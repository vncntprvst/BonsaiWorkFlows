# thought base and tip inverted when orientation flips?
# which would call for condition
	vSortRegionList[blob1Index].Orientation<0
# but turns out it's just that array item 0 corresponds to the highest y value instead of the smallest x
# Need to sort point list 

def FindBasePoint(inputPointArray):
  pointList = Enumerable.OrderBy(inputPointArray, lambda x:x.X)
  firstPoint = Enumerable.First(pointList)
  return firstPoint

def FindTipPoint(inputPointArray):
  pointList = Enumerable.OrderByDescending(inputPointArray, lambda x:x.X)
  lastPoint = Enumerable.First(pointList)
  return lastPoint

# Now, sorting list of components by centroid Y (or X) leads to identity inversion
# Instead of
vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Centroid.Y))
# Sort by base Y (or X)
vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).Y))

## Could use MinBy operator ? 
## Could also determine the most extreme points along the contour
# extLeft = tuple(c[c[:, :, 0].argmin()][0])
# extRight = tuple(c[c[:, :, 0].argmax()][0])
# extTop = tuple(c[c[:, :, 1].argmin()][0])
# extBot = tuple(c[c[:, :, 1].argmax()][0])

# Or use Orientation, which works mostly fine
#vSortRegionList = list(Enumerable.OrderByDescending(sortedRegions, lambda x:x.Orientation))

