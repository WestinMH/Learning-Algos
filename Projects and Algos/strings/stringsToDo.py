
# Remove the blanks/spaces from a given string
def removeBlanks(str):
    new_str = ""
    for i in range(len(str)):
        if str[i] != " ":
            new_str += (str[i])
    print(new_str)
removeBlanks("M ay th efo rcebew i thyou")

# Given a string return a string of just the included intergers
def getDigits(str):
    newString = ""
    for i in range (len(str)):
        if str[i].isdigit():
            newString += str[i]
    print(newString)
getDigits("1g2h3j4j5k6k7l9l0k")

# return an acronym of the first letters of each word in a given string
def acronym(str):
    str_list = str.split()
    acronym = ""
    for i in range (len(str_list)):
        words = str_list[i]
        acronym +=(words[0][0])
    print(acronym.upper())
acronym("May the force be with you")

# zip together the positionally associated values of two arrays
def zipper(list1,list2):
    associate = {}
    for i in range (len(list1)):
        associate[list1[i]] = list2[i]
    print(associate)
zipper(["number", 2, "greeting"], [22, "two", "Heyo!"])

# convert the keys to values and the values to keys in any given dictionary
def invertHash(assocArr):
    newDict = {}
    for k, v in  assocArr.items():
        newDict[v] = k
    print(newDict)
invertHash({'number': 22, 2: 'two', 'greeting': 'Heyo!'})






        # first = assocArr['']
        # second = assocArr[i+1]
        # assocArr[i+1] = first
        # assocArr[i] = second