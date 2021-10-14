def binary_search(L,x):
    """Binary search algorithm to find target x in list L
       cost: O(log_2(N)) since if we double the number of elem in the list, the number of iterations needed only increases by one 
       (as halfing the list is one iter). 
    """ 
    
    #Set initial start and end indices for full list
    istart = 0
    iend = len(L)-1
    #Contract "active" portion of list
    while istart<=iend:
        imid = int(0.5*(istart+iend))
        if x==L[imid]:
            return imid
        elif x < L[imid]:
            #cut off right half of list
            iend = imid-1
        else:
            #cut off left half of list
            istart = imid+1
        #we keep spliting and cutting untill we land on element we are looking for.
        #we keep track of element index through imid
    return -1


if __name__ == "__main__":
    L = [1,4, 6, 13, 35, 66, 79, 89, 90]
    #set target
    x = 89

    print(f"index of element {x} is {binary_search(L, x)}")
