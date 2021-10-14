
def merge(L,R):

    # two half lists which are already sorted - we are going to merge them
    
    n = len(L)
    M = []

    #indices 
    iL = 0
    iR = 0

    # n is the len of each sub list. We therfore iterate 2n times.
    for i in range(2*n):
    
        #compare iL and iR elements of L and R.
        #place the smaller elm in M and increment iL or iR resp.
    
    #FOR L    
        if L[iL]<R[iR]:
            M.append(L[iL])
            iL = iL + 1
            
            #check if we have reached end of list L.
            if iL==n:
                # add all remaining elements of R to M
                M.extend(R[iR:])
                break
            
    #For R
        else:
            M.append(R[iR])
            iR = iR + 1

            #check if we have reached end of list R
            if iR==n:
                # add all remaining elements of L to M
                M.extend(L[iL:])
                break
    return M

#example
if __name__ == "__main__":
    L = [2, 6, 24, 56]
    R = [8, 23, 31, 54]
    M = merge(L,R)
    print(M)
