# Matrix-Patter-Fill-2
Recursive function which goes through an empty matrix passed to it which has many levels of inner matrices with varying depths, all of them being empty.

Input (global values): strVal = “abcdefghijk”, PAT_LEN = someInt (some +ve int)
• The program needs to fill in the pattern as per the values in the above identifiers.
• The rules to be followed are the following:
1. Assuming the above value is in strVal, after ‘k’ is filled into an empty list, it should
wrap around from ‘a’. Note: The string used, needs to be configurable manually.
2. You are free to follow my implementation (outerChkMyMatrix) discussed in the
Session 17 or your own as the starting point, but it needs to use inner functions with
recursion.
3. You can assume that the list object passed to the function has sub-lists, which are all
empty.
4. Returns the same list object back which is filled in with the pattern as per
configuration values.
5. You can now use the filled in matrix to test the outerChkMyMatrix() code too.
