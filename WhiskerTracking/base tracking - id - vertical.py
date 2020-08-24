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
baseDistThd = 15
#centroidDistThd = 100
numWhiskers = 0
targetWhisker = 1
baseList = []
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
	global noWhisker, whiskerIndex, initialBase, currBase, firstPass, numWhiskers, baseList, baseDistList  #, currCentroid
	# Order whisker components list by base point, bottom to top
	#vSortWhiskers = list(Enumerable.OrderByDescending(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).Y))
	vSortWhiskers = list(Enumerable.OrderBy(sortedRegions, lambda x:FindBasePoint(x.Contour.ToArray[Point]()).Y))

	if noWhisker is True: #on first pass
		if len(vSortWhiskers) >= (1 + targetWhisker) and firstPass == True:
			print("init")
			whiskerIndex = targetWhisker
			initialBase = currBase = FindBasePoint(vSortWhiskers[whiskerIndex].Contour.ToArray[Point]())
			#currCentroid = vSortWhiskers[whiskerIndex].Centroid
			numWhiskers = len(vSortWhiskers)
			firstPass = False
		elif len(vSortWhiskers) < 1:
			print("still no whiskers")
		
	# Compare base points and find closest base, within spatial treshold limits (typically, either index 0 or 1)
	# ToDo: need to find what to do when tracked whisker has jumped to a neigboring one.  
	if len(vSortWhiskers) >= 1:
		#baseDist=baseDistThd
		#centroidDist=centroidDistThd
		#bestIdx=whiskerIndex
		baseList[:] = []
		baseDistList[:] = [] 
		#centroidDistList = []
		for wIdx, wCComp in enumerate(vSortWhiskers):
			thatBase = FindBasePoint(wCComp.Contour.ToArray[Point]())
			baseDist = DistBetweenPoints(currBase, thatBase)
			if baseDist < baseDistThd: # add it
				baseList.append(thatBase)
				baseDistList.append(baseDist)
			else:
				baseList.append(None)
				baseDistList.append(None)
		#listnans = lambda array: any(filter(math.isnan, baseDistList)) #math.isnan(baseDistList))
		listNotNones = [i for i, item in enumerate(baseDistList) if item is not None]
		print("baseDistList", baseDistList, "isnotnone", listNotNones)
		#vSortWhiskers = [vSortWhiskers[i] for i in listnotnones]
		if len(listNotNones) > 0:
			baseList = [baseList[i] for i in listNotNones]
			baseDistList = [baseDistList[i] for i in listNotNones]
			
				#thatCentroid = wCComp.Centroid
				#centroidDistList.append(DistBetweenPoints(currCentroid, thatCentroid))
				#print("whisker", wIdx, "baseX", thatBase.X, "distance", DistBetweenPoints(currBase, thatBase))
			
			#if len(vSortWhiskers) == numWhiskers and baseDistList[targetWhisker]<baseDistThd:
			#	bestIdx = targetWhisker
			#else:
			#	bestIdx = baseDistList.index(min(baseDistList)) 
			#print("bestBaseIdx", bestBaseIdx)
			#print("selecting Idx")
			if len(baseDistList) == numWhiskers and len(baseDistList) > whiskerIndex and baseDistList[whiskerIndex]<baseDistThd: #len(baseDistList) == numWhiskers and 
				bestIdx = whiskerIndex
				#print("option 1, bestIdx is", bestIdx)
			elif len(baseDistList) > numWhiskers: # e.g., whiskers have fused, then unfused
				baseDistList[:] = []
				for thatBase in baseList:
					baseDist = DistBetweenPoints(initialBase, thatBase)
					baseDistList.append(baseDist)
				bestIdx = baseDistList.index(min(baseDistList))
			else:
				bestIdx = baseDistList.index(min(baseDistList))
				#print("option 3, bestIdx is", bestIdx)

			if Single.IsNaN(whiskerIndex) == True:
				#bestIdx = bestBaseIdx
				whiskerIndex = bestIdx
			# check that nothing is amiss for big base jumps or changes in index
			# thatBase = FindBasePoint(vSortWhiskers[bestBaseIdx].Contour.ToArray[Point]())
			# if DistBetweenPoints(currBase, thatBase) > baseDist or bestBaseIdx!=whiskerIndex: #check if centroid is also compatible
			# 	print("centroid based check because", DistBetweenPoints(currBase, thatBase) > baseDist , bestBaseIdx!=whiskerIndex)
			# 	centroidDistList = [] 
			# 	for wIdx, wCComp in enumerate(vSortWhiskers):
			# 		thatCentroid = wCComp.Centroid
			# 		centroidDistList.append(DistBetweenPoints(currCentroid, thatCentroid))
			# 		#print("whisker", wIdx, "centroidX", thatCentroid.X, "distance", DistBetweenPoints(currCentroid, thatCentroid))
			# 	bestCentroidIdx = centroidDistList.index(min(centroidDistList))
			# 	print("Best centroid is whisker", bestCentroidIdx)
			# 	# But careful: could be that the whisker has disappeared, or reappeared
			# 	if bestBaseIdx!=bestCentroidIdx: #resolve
			# 		if len(vSortWhiskers)<numWhiskers:
			# 			print("Conflict with best base. Use centroid index", bestCentroidIdx)
			# 			bestIdx = bestCentroidIdx #be conservative
			# 		else:
			# 			print("Conflict with best base. Keep current index", whiskerIndex)
			# 			bestIdx = whiskerIndex #be conservative
			# 	else:
			# 		if len(vSortWhiskers) == numWhiskers:
			# 			print("No conflict, no whisker number change so keep current index", whiskerIndex)
			# 			bestIdx = whiskerIndex #be conservative
			# 		else:
			# 			print("No conflict but whisker number change so use base index", bestBaseIdx)
			# 			bestIdx = bestBaseIdx #       
			# else:
			# 	bestIdx = bestBaseIdx
			#print("whisker Index is now", bestIdx)
			#if bestIdx!=whiskerIndex:
			#	print("Jump!")
			#vSortWhiskers = [vSortWhiskers[i] for i in listNotNones]
			print("get base from candidate whisker",bestIdx,"among",len(baseList))
			thatBase = baseList[bestIdx] #FindBasePoint(vSortWhiskers[bestIdx].Contour.ToArray[Point]())
			baseDist = baseDistList[bestIdx] #DistBetweenPoints(currBase, thatBase)
			if baseDist < 2*baseDistThd:
				#print("selected whisker is ", bestIdx)
				whiskerIndex = bestIdx
				currBase = thatBase
				#currCentroid = vSortWhiskers[whiskerIndex].Centroid
			else:
				#print("no whisker selected")
				whiskerIndex = float.NaN
			noWhisker = False
		else:
			noWhisker = True
			whiskerIndex = float.NaN
	else:
		# if no whisker components, return nan
		#print("no whisker present")
		noWhisker = True
		whiskerIndex = float.NaN
	# Keep track of the number of whiskers
	#numWhiskers=len(vSortWhiskers)
	numWhiskers=len(baseDistList)

 	# Create whisker component
	Component = ConnectedComponentCollection(sortedRegions.ImageSize)
	if Single.IsNaN(whiskerIndex) == False:
		#print("creating component")
		Component.Add(vSortWhiskers[int(listNotNones[whiskerIndex])])
		
	return Component