import numba
from unyt import unyt_array as ar

@numba.njit
def create_numba_hashtable(left, right):

    output = dict()

    for i in range(left.size):
        output[left[i]] = right[i]

    return output

x = create_numba_hashtable(ar([1,2,3]), ar([4,5,6]))
for i in x.values():
    print(i)