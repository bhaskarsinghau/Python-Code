#Convert nested list into one list, just by using Itertools one line of code.
#Example – [[1, 2], [3, 4], [5, 6]] should be converted into [1, 2, 3, 4, 5, 6]

import itertools 
a = [[1, 2], [3, 4], [5, 6]] 
print(list(itertools.chain.from_iterable(a))) 
