

def countNumbers(nums):
    arrCounted = []
    prev = None
    for element in nums:
        if element != prev:
            arrCounted.append(str(element)+':'+str(1))
            prev = element
        else:
            prevSplited = arrCounted[len(arrCounted) - 1].split(':')
            arrCounted[len(arrCounted) - 1] = prevSplited[0]+':'+str(int(prevSplited[1])+1)
    return arrCounted


def packNumbers(arrNum):
    def formalList(x):
        elementsplit = x.split(":")
        if elementsplit[1] == "1":
            return int(elementsplit[0])
        else:
            return elementsplit[0]+":"+elementsplit[1]

    if len(arrNum) > 0:
        arrCounted = countNumbers(arrNum)
        return map(formalList, arrCounted)
    else:
        return []
        

if __name__ == "__main__":
    print(packNumbers([9, 9, 1, 5, 5, 5, 9]))
