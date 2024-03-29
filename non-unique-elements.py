#Your optional code here
#You can import some modules or create additional functions


def checkio(data: list) -> list:
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  
    # return [lis for lis in data if data.count(lis) > 1]
    '''
    lis = []
    for x in data:
        if data.count(x) > 1:
            lis.append(x)
    return[lis]
    '''
checkio([1,2,3,3,2,1])
    #replace this for solution
    #return data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
