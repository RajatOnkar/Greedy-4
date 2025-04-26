# Greedy-4

## Problem1: Minimum Path Form String formation

# https://leetcode.com/problems/shortest-way-to-form-string/

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

# Binary Search solution
# Initialize a hashmap and store all elements of the source as key and the occurences in the string as
# values in the map
# While the target pointer is less than target length parse over the target array to check if the 
# character exists in the source string. If not return -1
# Get the keys for the particular source character and run the closest binary search to get the index
# If we are at the end of the List then we restart the search and increment the count of substrings
# Else we increment the source pointer with the binary search index and target pointer
# Return the final count

## Problem2:  Equal Row From Minimum Domino Rotations 

# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

# Hashmap Solution
# Initializa a hashmap and target as '1'
# Iterate over the tops and bottoms array and find the frequency of all numbers to store in a hashmap
# The highest frequency element is stored as top and bottom and calculate the rotations from tops and
# bottoms.
# Return the minimum rotations either from tops and bottoms 

# Pair elements solution
# Create a check function that will check if the most frequent element which is the target is either in
# the tops or bottoms array
# Calculate the rotations and return the minimum rotations required
# For any pair if the elements are not in the tops or bottoms array then we cannot have an equal row
# of all elements
# We start with the first element from tops and then first element of the bottoms (we can choose any 
# pair to get the equal row of all elements)