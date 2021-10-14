def iter_sort(L):
    """Iteratively sorts elements in a list starting at index 0
    """
    for j in range(1,len(L)):
    #compare L[j] with L[i]
        i = j-1
        current_elm = L[j] 
        while i>=0:
            if current_elm<L[i]: #shift from i to i-1
                i=i-1
                if i<0: #unless i is already 0
                    L[i+2:j+1] = L[i+1:j]
                    L[i+1] = current_elm
            else: #insert current_elm at i+1
                L[i+2:j+1] = L[i+1:j] # make space for element
                L[i+1] = current_elm
                i = -1

    return L


if __name__ == "__main__":
    L = [66,5,34,13,88,45,4]
    print(iter_sort(L))