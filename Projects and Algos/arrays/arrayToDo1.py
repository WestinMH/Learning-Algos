import random

# randomize the order of any given array/list v
def shuffle(list):
    new_list = []
    for i in range (0, len(list), 1):
        randomIndex = random.randint(0, len(list)-1)
        new_list.append(list[randomIndex])
        temp = list[randomIndex]
        list[randomIndex] = list[len(list)-1]
        list[len(list)-1] = temp
        list.pop()
    return new_list
print(shuffle([5,3,1,2,4,6]))

#  Return array containing heights of buildings you can see, 
# in order. Given [-1,1,1,7,3,12] return [1,7,12]. Given [0,4] return [4].
#  As always with challenges, do not use built-in array functions such as unshift().
def skyline(list):
    newList = []
    highestBuilding = 0
    for i in range (0,len(list), 1):
        if list[i] > highestBuilding:
            newList.append(list[i])
        highestBuilding = list[i]
    return newList
print(skyline([-3,1,4,6,2,8,5,10,222]))

# Given two arrays/lists combine them sequencially-like a zipper.
def zipper(list1, list2):
    mergedLists = []
    
    if len(list1) > len(list2):
        for i in range (len(list2)):
            mergedLists.append(list1[i])
            mergedLists.append(list2[i])
        for i in range (len(list1)-len(list2)):
            mergedLists.append(list1[i+len(list2)])
    else:
        for i in range (len(list1)):
            mergedLists.append(list1[i])
            mergedLists.append(list2[i])
    return mergedLists
print(zipper([1,3,5,7,200,201,202],[2,4,6,8]))

