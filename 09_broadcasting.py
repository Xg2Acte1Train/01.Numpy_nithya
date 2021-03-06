import numpy as np

"""
What is the shape of the broadcasting array resulted from arrays with shapes (4, 1, 1,7) and (3, 1)?

Given: s1 = (4, 3); s2 = (3,)
Step 1 and 2: s1 = (4, 3); s2 = (1, 3)
Step 3 and 4: pass in 2 dimensions
Result : Broadcasting feasible;
         resulted array shape - (4,3) 
         
Given: s1 = (5,); s2 = (5,4,3)
Step 1 and 2: s1 = (1, 1, 5); s2 = (5, 4, 3)
Step 3 and 4: fail in last dimension. ( 5 != 3)
Result : Broadcasting not feasible. 
"""
