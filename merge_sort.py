#import merge_module to utilise merge algorithm
import merge_module

def msort(A):
    """ Implementation of merge sort algorithm which takes an unsorted list A and applies recussion to split the list untill 
    we have nn lists of length 1. Then merges (through merge algorithm) these lists pairwise back up the stack list, untill 
    we are left with single sorted list of nn elements.
    """
    
    nn = len(A)
    if nn==1:
        return A
    else: # split list and call msort in a recursive fashion on left and right lists
        split = int(nn/2)
        L = msort(A[:split]) # by calling msort again we keep split the list untill we get len one!
        R = msort(A[split:]) # then we merge our way back up - through power of recursion (ie 1n1 become 2, 2n2 become 4, ...)
        M = merge_module.merge(L, R)
        return M

if __name__ == "__main__":
    A = [1,12,34,2,14,24,5,6] # list has to be powers of 2 ie 2, 4, 8, 16, 32, .... so that the spliting works! (can be fixed) 
    sorter = msort(A)
    print(sorter)
