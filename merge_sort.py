#import merge_module to utilise merge algorithm
import merge_module

def msort(A):
    nn = len(A)
    if nn==1:
        return A
    else: # split list and call msort in a recursive fashion on left and right lists
        split = int(nn/2)
        L = msort(A[:split]) # by calling msort again we keep split the list untill we get len one!
        R = msort(A[split:]) # then we merge our way back up the list - through power of recursion
        M = merge_module.merge(L, R)
        return M

if __name__ == "__main__":
    A = [1,12,34,2,14,24,5,6] # list has to be powers of 2 ie 2, 4, 8, 16, 32, .... so that the spliting works! (can be fixed) 
    sorter = msort(A)
    print(sorter)
