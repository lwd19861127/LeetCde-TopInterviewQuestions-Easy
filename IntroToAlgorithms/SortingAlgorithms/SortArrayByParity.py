def sortArrayByParity(A):
    if len(A) <= 1:
        return A
    # devide
    left = A[:len(A)//2]
    right = A[len(A)//2:]
    even_left = sortArrayByParity(left)
    odd_right = sortArrayByParity(right)

    return merge_even_odd(even_left, odd_right)


def merge_even_odd(A, B):
    i = 0
    j = 0
    merged = []
    while i < len(A):
        if A[i] % 2 == 0:
            merged = [A[i]] + merged
        else:
            merged = merged + [A[i]]
        i += 1
    while j < len(B):
        if B[j] % 2 == 0:
            merged = [B[j]] + merged
        else:
            merged = merged + [B[j]]
        j += 1
    return merged


