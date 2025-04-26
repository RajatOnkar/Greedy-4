'''
// Time Complexity :
# Problem 1 - O(n) length of the tops / bottoms frequency (Hashmap solution)
            - O(n) (Pair elements solution) 
# Problem 2 - O(m*n) m - length of source string, n - length of target string (Two pointers)
            - O(mlogn) (Binary Search)
// Space Complexity :
# Problem 1 - O(n) To store in hashmap and O(1) for lookup, O(1) as we pick only pairs
# Problem 2 - O(n) To store all the source characters in the map
// Did this code successfully run on Leetcode :
# Yes the code ran successfully.

// Any problem you faced while coding this :

// Your code here along with comments explaining your approach
'''
# Problem 1 - Minimum Path Form String formation

# Two Pointers 
# Initialize an hashset and store the characters of the source string
# Initialize the count as '1' and we parse the target string and check if the target string characters
# exist in the hashset, if none of the characters match return -1 as we cannot make substrings
# When the source and the target character matches we increment both the source and target pointers 
# along with the count
# If target reaches its length then we return the final count as output else move the source pointer
# If we reach the end of the source string then we start parsing the source string again by reseting the
# source pointer and incrementing the count
# Return the final count of all possible substrings

class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        set_1 = set(source)
        s1 = len(source); t1 = len(target)       
        count = 1
        sp = 0; tp = 0
        while tp < len(target):
            tChar = target[tp]
            if tChar not in set_1:
                return -1
            sChar = source[sp]
            if sChar == tChar:
                sp += 1
                tp += 1
                if tp == t1:
                    return count
            else:
                sp += 1
            if sp == s1:
                sp = 0
                count += 1
        return count

# Binary Search solution
# Initialize a hashmap and store all elements of the source as key and the occurences in the string as
# values in the map
# While the target pointer is less than target length parse over the target array to check if the 
# character exists in the source string. If not return -1
# Get the keys for the particular source character and run the closest binary search to get the index
# If we are at the end of the List then we restart the search and increment the count of substrings
# Else we increment the source pointer with the binary search index and target pointer
# Return the final count

class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        from collections import defaultdict
        map_1 = defaultdict(list)
        s1 = len(source); t1 = len(target) 

        for i in range(s1):
            c = source[i]
            map_1[c].append(i)

        count = 1
        sp = 0; tp = 0
        while tp < t1:
            tChar = target[tp]
            if tChar not in map_1:
                return -1
            
            li = map_1[tChar]
            bsIdx = self.binarysearch(li, sp)

            if bsIdx == len(li):
                count += 1
                sp = 0
            else:
                sp = li[bsIdx] + 1
                tp += 1

        return count
    
    def binarysearch(self, li, target):
        low = 0; high = len(li) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if li[mid] < target:
                low = mid + 1 
            else:
                high = mid - 1
        return low    

## Problem 2 - Equal Row From Minimum Domino Rotations

# Hashmap Solution
# Initializa a hashmap and target as '1'
# Iterate over the tops and bottoms array and find the frequency of all numbers to store in a hashmap
# The highest frequency element is stored as top and bottom and calculate the rotations from tops and
# bottoms.
# Return the minimum rotations either from tops and bottoms 

class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        map_1 = {}
        target = 1
        m = len(tops); n = len(bottoms)
        for i in range(m):
            top = tops[i]
            if top not in map_1:
                map_1[top] = 1
            else:
                map_1[top] += 1
        
            if map_1[top] >= m:
                target = top
                break

            bottom = bottoms[i]
            if bottom not in map_1:
                map_1[bottom] = 1
            else:
                map_1[bottom] += 1
        
            if map_1[bottom] >= m:
                target = bottom
                break
        
        aRot = 0
        bRot = 0
        for i in range(m):
            top = tops[i]
            bottom = bottoms[i]
            if top != target and bottom != target:
                return -1
            if top != target:
                aRot += 1
            if bottom != target:
                bRot += 1
        return min(aRot, bRot)  

# Pair elements solution
# Create a check function that will check if the most frequent element which is the target is either in
# the tops or bottoms array
# Calculate the rotations and return the minimum rotations required
# For any pair if the elements are not in the tops or bottoms array then we cannot have an equal row
# of all elements
# We start with the first element from tops and then first element of the bottoms (we can choose any 
# pair to get the equal row of all elements)

class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        a = tops[0]
        result = self.check(tops, bottoms, a)
        if result != -1:
            return result
        b = bottoms[0]
        return self.check(tops, bottoms, b)

    def check(self, tops, bottoms, target):
        aRot = 0
        bRot = 0
        for i in range(len(tops)):
            top = tops[i]
            bottom = bottoms[i]
            if top != target and bottom != target:
                return -1
            if top != target:
                aRot += 1
            if bottom != target:
                bRot += 1
        return min(aRot, bRot)  
