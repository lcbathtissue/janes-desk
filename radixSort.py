def radixSort_cntSort(inputArray, placeValue):
    # We can assume that the number of digits used to represent
    # all numbers on the placeValue position is not grater than 10
    countArray = [0] * 10
    inputSize = len(inputArray)

    # placeElement is the value of the current place value
    # of the current element, e.g. if the current element is
    # 123, and the place value is 10, the placeElement is
    # equal to 2
    for i in range(inputSize):
        placeElement = (inputArray[i].getGrade() // placeValue) % 10
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i - 1]

    # Reconstructing the output array
    outputArray = [0] * inputSize
    i = inputSize - 1
    while i >= 0:
        currentEl = inputArray[i]

        # !! ORIGINAL CODE, EDITS BELOW
        # placeElement = (inputArray[i] // placeValue) % 10

        # <EDITS: aldenocain / Alden O'Cain>
        placeElement = (inputArray[i].getGrade() // placeValue) % 10
        # </EDITS: aldenocain / Alden O'Cain>

        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray
def radixSort(inputArray):
    # Step 1 -> Find the maximum element in the input array

    # !! ORIGINAL CODE, EDITS BELOW
    # maxEl = max(inputArray)

    # <EDITS: aldenocain / Alden O'Cain>
    maxEl = 0
    for paper in inputArray:
        paperGrade = paper.getGrade()
        if paperGrade > maxEl:
            maxEl = paperGrade
    # </EDITS: aldenocain / Alden O'Cain>

    # Step 2 -> Find the number of digits in the `max` element
    D = 1
    while maxEl > 0:
        maxEl /= 10
        D += 1

    # Step 3 -> Initialize the place value to the least significant place
    placeVal = 1

    # Step 4
    outputArray = inputArray
    while D > 0:
        outputArray = radixSort_cntSort(outputArray, placeVal)
        placeVal *= 10
        D -= 1

    return outputArray
