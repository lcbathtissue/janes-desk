# USED FOR TESTING AND CONFIRMATION
# OF THE OUTPUT OF OUR ALGORITHM
from copy import copy

def findNTrueMaxes(papers, num_maxes):
    papers = copy(papers)  # duplicates object otherwise python will mutate
    found_maxes = []
    while num_maxes > 0:
        nextMaxRet = findNextTrueMax(papers)  # ret: papers, maxGrade
        papers = nextMaxRet[0]  # papers with max removed
        found_maxes.append(nextMaxRet[1])  # max that was removed
        num_maxes -= 1
    return found_maxes  # return the N max values, not the papers

def findNextTrueMax(papers):
    maxGrade = 0
    maxIndex = 0
    for index, paper in enumerate(papers):
        paperGrade = paper.getGrade()
        if paperGrade > maxGrade:
            maxGrade = paperGrade
            maxIndex = index
    papers.pop(maxIndex)
    return [ papers, maxGrade ]
