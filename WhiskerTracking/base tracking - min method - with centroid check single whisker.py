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
firstPass = True
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
	global noWhisker, whiskerIndex, currBase, currCentroid, firstPass
	# Order whisker components list by base point, bottom to top
	#vSortWhiskers = list(Enumerable.OrderByDescending(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).Y))
	hSortWhiskers = list(Enumerable.OrderBy(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).X))

	if noWhisker is True: #on first pass
		if len(hSortWhiskers) >= 2 and firstPass == True:
			print("init")
			whiskerIndex = 1
			currBase = FindBasePoint(hSortWhiskers[whiskerIndex].Contour.ToArray[Point]())
			currCentroid = hSortWhiskers[whiskerIndex].Centroid
			firstPass = False
		else:
			print("still no whiskers")
		
	# Compare base points and find closest base, within spatial treshold limits (typically, either index 0 or 1)
	# ToDo: need to find what to do when tracked whisker has jumped to a neigboring one.  
	if len(hSortWhiskers) >= 1:
		baseDist=baseDistThd
		centroidDist=centroidDistThd
		#bestIdx=whiskerIndex
		baseDistList = [] 
		for wIdx, wCComp in enumerate(hSortWhiskers):
			thatBase = FindBasePoint(wCComp.Contour.ToArray[Point]())
			baseDistList.append(DistBetweenPoints(currBase, thatBase))
			#print("whisker", wIdx, "baseX", thatBase.X, "distance", DistBetweenPoints(currBase, thatBase))
		bestBaseIdx = baseDistList.index(min(baseDistList)) 
		print("bestBaseIdx", bestBaseIdx)
		# check that nothing is amiss for big base jumps or changes in index
		thatBase = FindBasePoint(hSortWhiskers[bestBaseIdx].Contour.ToArray[Point]())
		if DistBetweenPoints(currBase, thatBase) > baseDist or bestBaseIdx!=whiskerIndex: #check if centroid is also compatible
			print("centroid based check")
			centroidDistList = [] 
			for wIdx, wCComp in enumerate(hSortWhiskers):
				thatCentroid = wCComp.Centroid
				centroidDistList.append(DistBetweenPoints(currCentroid, thatCentroid))
				print("whisker", wIdx, "centroidX", thatCentroid.X, "distance", DistBetweenPoints(currCentroid, thatCentroid))
			bestCentroidIdx = centroidDistList.index(min(centroidDistList))
			print("Jump! Best centroid is whisker", bestCentroidIdx)	
			# But careful: could be that the whisker has disappeared

			if bestBaseIdx!=bestCentroidIdx: #resolve
				print("Conflict with best base. Keep current index", whiskerIndex)
				bestIdx = whiskerIndex #be conservative
			else:
				bestIdx = bestBaseIdx #fine          
		else:
			bestIdx = bestBaseIdx
		#print("whisker Index is now", bestIdx)
		thatBase = FindBasePoint(hSortWhiskers[bestIdx].Contour.ToArray[Point]())
		baseDist = DistBetweenPoints(currBase, thatBase)
		if baseDist < 2*baseDistThd:
			print("selected whisker is ", bestIdx)
			whiskerIndex = bestIdx
			currBase = thatBase
			currCentroid = hSortWhiskers[whiskerIndex].Centroid
		else:
			print("no whisker selected")
			whiskerIndex = float.NaN
		noWhisker = False
	else:
		# if no whisker components, return nan
		print("no whisker present")
		noWhisker = True
		whiskerIndex = float.NaN

 
	Component = ConnectedComponentCollection(sortedRegions.ImageSize)
	if Single.IsNaN(whiskerIndex) == False:
		#print("creating component")
		Component.Add(hSortWhiskers[int(whiskerIndex)])
		
	return Component