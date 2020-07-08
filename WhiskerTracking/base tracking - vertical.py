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
#NaNPoint = Point2f(float.NaN,float.NaN)
baseDistThd = 20
targetWhisker = 1
baseDistList = []

def FindBasePoint(inputPointArray):
	pointList = Enumerable.OrderBy(inputPointArray, lambda x:x.X) #X point for vertical head position
	firstPoint = Enumerable.First(pointList)
	return firstPoint

def DistBetweenPoints(pt1,pt2):
	dx = abs(pt2.X - pt1.X)
	dy = abs(pt2.Y - pt1.Y)
	# distance vector
	return math.sqrt(dx**2 + dy**2)

@returns(ConnectedComponentCollection)
def process(sortedRegions):
	global noWhisker, whiskerIndex, initialBase, firstPass, baseDistList  #, currCentroid
	# Order whisker components list by base point, bottom to top
	#vSortWhiskers = list(Enumerable.OrderByDescending(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).Y))
	vSortWhiskers = list(Enumerable.OrderBy(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).Y))

	if noWhisker is True: #on first pass
		if len(vSortWhiskers) >= (1 + targetWhisker) and firstPass == True:
			print("init")
			whiskerIndex = targetWhisker
			initialBase = FindBasePoint(vSortWhiskers[whiskerIndex].Contour.ToArray[Point]())
			firstPass = False
		elif len(vSortWhiskers) < 1:
			print("still no whiskers")
			
	# Compare base points and find closest base, within spatial treshold limits (typically, either index 0 or 1)
	# ToDo: need to find what to do when tracked whisker has jumped to a neigboring one.  
	if len(vSortWhiskers) >= 1:
		baseDistList[:] = [] 
		for wIdx, wCComp in enumerate(vSortWhiskers):
			thatBase = FindBasePoint(wCComp.Contour.ToArray[Point]())
			baseDist = DistBetweenPoints(initialBase, thatBase)
			if baseDist < baseDistThd: # add it
				baseDistList.append(baseDist)
			else:
				baseDistList.append(None)
		listNotNones = [i for i, item in enumerate(baseDistList) if item is not None]
		#print("baseDistList", baseDistList, "isnotnone", listNotNones)
		if len(listNotNones) > 0:
			baseDistList = [baseDistList[i] for i in listNotNones]
			whiskerIndex = baseDistList.index(min(baseDistList))
		else:
			noWhisker = True
			whiskerIndex = float.NaN
	else:
		noWhisker = True
		whiskerIndex = float.NaN

	# Create whisker component
	Component = ConnectedComponentCollection(sortedRegions.ImageSize)
	if Single.IsNaN(whiskerIndex) == False:
		#print("creating component")
		Component.Add(vSortWhiskers[int(listNotNones[0])])
		if len(listNotNones)>1:
			Component.Add(vSortWhiskers[int(listNotNones[1])])
		if len(listNotNones)>2:
				Component.Add(vSortWhiskers[int(listNotNones[2])])

	return Component