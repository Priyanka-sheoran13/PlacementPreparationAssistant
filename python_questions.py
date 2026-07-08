python_questions = [

{
    "title": "Two Sum",
    "difficulty": "Medium",
    "topic": "Array, Hash Map",
    "description": "Given an array of integers nums and an integer target, return the indices of the two numbers whose sum equals the target.",
    "input": "nums = [2,7,11,15], target = 9",
    "output": "[0,1]",
    "solution": """def twoSum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i"""
},

{
    "title": "Longest Substring Without Repeating Characters",
    "difficulty": "Medium",
    "topic": "String, Sliding Window",
    "description": "Find the length of the longest substring without repeating characters.",
    "input": 's = "abcabcbb"',
    "output": "3",
    "solution": """def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    ans = 0

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right
        ans = max(ans, right-left+1)

    return ans"""
},

{
    "title": "Maximum Subarray Sum",
    "difficulty": "Medium",
    "topic": "Array, Kadane Algorithm",
    "description": "Find the contiguous subarray having the largest sum.",
    "input": "[-2,1,-3,4,-1,2,1,-5,4]",
    "output": "6",
    "solution": """def maxSubArray(nums):

    current = nums[0]
    maximum = nums[0]

    for i in nums[1:]:

        current = max(i,current+i)

        maximum = max(maximum,current)

    return maximum"""
},

{
    "title": "Merge Intervals",
    "difficulty": "Medium",
    "topic": "Intervals",
    "description": "Merge all overlapping intervals.",
    "input": "[[1,3],[2,6],[8,10],[15,18]]",
    "output": "[[1,6],[8,10],[15,18]]",
    "solution": """def merge(intervals):

    intervals.sort()

    result=[intervals[0]]

    for start,end in intervals[1:]:

        if start<=result[-1][1]:

            result[-1][1]=max(result[-1][1],end)

        else:

            result.append([start,end])

    return result"""
},

{
    "title": "Binary Search",
    "difficulty": "Medium",
    "topic": "Searching",
    "description": "Implement Binary Search in a sorted array.",
    "input": "nums=[1,2,3,4,5], target=4",
    "output": "3",
    "solution": """def binarySearch(nums,target):

    left=0
    right=len(nums)-1

    while left<=right:

        mid=(left+right)//2

        if nums[mid]==target:

            return mid

        elif nums[mid]<target:

            left=mid+1

        else:

            right=mid-1

    return -1"""
},

{
    "title": "Rotate Array",
    "difficulty": "Medium",
    "topic": "Array",
    "description": "Rotate the array to the right by k steps.",
    "input": "nums=[1,2,3,4,5,6,7], k=3",
    "output": "[5,6,7,1,2,3,4]",
    "solution": """def rotate(nums,k):

    k%=len(nums)

    nums[:]=nums[-k:]+nums[:-k]"""
},
{
    "title": "Valid Parentheses",
    "difficulty": "Medium",
    "topic": "Stack",
    "description": "Given a string containing (), {}, and [], determine if the input string is valid.",
    "input": 's = "()[]{}"',
    "output": "True",
    "solution": """def isValid(s):
    stack = []
    d = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack.pop() != d[ch]:
                return False
    return len(stack) == 0"""
},

{
    "title": "Group Anagrams",
    "difficulty": "Medium",
    "topic": "Hash Map, String",
    "description": "Group all anagrams together.",
    "input": '["eat","tea","tan","ate","nat","bat"]',
    "output": '[["eat","tea","ate"],["tan","nat"],["bat"]]',
    "solution": """from collections import defaultdict

def groupAnagrams(strs):
    d = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        d[key].append(word)
    return list(d.values())"""
},

{
    "title": "Product of Array Except Self",
    "difficulty": "Medium",
    "topic": "Array",
    "description": "Return an array where each element is the product of all other elements.",
    "input": "[1,2,3,4]",
    "output": "[24,12,8,6]",
    "solution": """def productExceptSelf(nums):
    n = len(nums)
    ans = [1]*n

    left = 1
    for i in range(n):
        ans[i] = left
        left *= nums[i]

    right = 1
    for i in range(n-1,-1,-1):
        ans[i] *= right
        right *= nums[i]

    return ans"""
},

{
    "title": "Top K Frequent Elements",
    "difficulty": "Medium",
    "topic": "Hash Map",
    "description": "Return the k most frequent elements.",
    "input": "nums=[1,1,1,2,2,3], k=2",
    "output": "[1,2]",
    "solution": """from collections import Counter

def topKFrequent(nums,k):
    return [x for x,_ in Counter(nums).most_common(k)]"""
},

{
    "title": "Search in Rotated Sorted Array",
    "difficulty": "Medium",
    "topic": "Binary Search",
    "description": "Search a target in a rotated sorted array.",
    "input": "nums=[4,5,6,7,0,1,2], target=0",
    "output": "4",
    "solution": """def search(nums,target):
    l,r=0,len(nums)-1

    while l<=r:
        m=(l+r)//2

        if nums[m]==target:
            return m

        if nums[l]<=nums[m]:
            if nums[l]<=target<nums[m]:
                r=m-1
            else:
                l=m+1
        else:
            if nums[m]<target<=nums[r]:
                l=m+1
            else:
                r=m-1

    return -1"""
},

{
    "title": "Container With Most Water",
    "difficulty": "Medium",
    "topic": "Two Pointers",
    "description": "Find the maximum area of water a container can store.",
    "input": "[1,8,6,2,5,4,8,3,7]",
    "output": "49",
    "solution": """def maxArea(height):
    l=0
    r=len(height)-1
    ans=0

    while l<r:
        ans=max(ans,min(height[l],height[r])*(r-l))

        if height[l]<height[r]:
            l+=1
        else:
            r-=1

    return ans"""
},
{
    "title": "3Sum",
    "difficulty": "Medium",
    "topic": "Array, Two Pointers",
    "description": "Find all unique triplets in the array which gives the sum of zero.",
    "input": "nums=[-1,0,1,2,-1,-4]",
    "output": "[[-1,-1,2],[-1,0,1]]",
    "solution": """def threeSum(nums):
    nums.sort()
    ans=[]
    n=len(nums)

    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue

        l=i+1
        r=n-1

        while l<r:
            s=nums[i]+nums[l]+nums[r]

            if s==0:
                ans.append([nums[i],nums[l],nums[r]])

                while l<r and nums[l]==nums[l+1]:
                    l+=1

                while l<r and nums[r]==nums[r-1]:
                    r-=1

                l+=1
                r-=1

            elif s<0:
                l+=1
            else:
                r-=1

    return ans"""
},

{
    "title": "Longest Consecutive Sequence",
    "difficulty": "Medium",
    "topic": "Hash Set",
    "description": "Find the length of the longest consecutive elements sequence.",
    "input": "[100,4,200,1,3,2]",
    "output": "4",
    "solution": """def longestConsecutive(nums):
    s=set(nums)
    longest=0

    for num in s:
        if num-1 not in s:
            length=1

            while num+length in s:
                length+=1

            longest=max(longest,length)

    return longest"""
},

{
    "title": "Find Duplicate Number",
    "difficulty": "Medium",
    "topic": "Array",
    "description": "Find the duplicate number in an array containing n+1 integers.",
    "input": "[1,3,4,2,2]",
    "output": "2",
    "solution": """def findDuplicate(nums):
    seen=set()

    for i in nums:
        if i in seen:
            return i
        seen.add(i)"""
},

{
    "title": "Word Search",
    "difficulty": "Medium",
    "topic": "Backtracking",
    "description": "Given a 2D board and a word, determine if the word exists in the grid.",
    "input": 'board=[["A","B"],["C","D"]], word="AB"',
    "output": "True",
    "solution": """# DFS + Backtracking Solution"""
},

{
    "title": "Number of Islands",
    "difficulty": "Medium",
    "topic": "Graph, DFS",
    "description": "Count the number of islands in a 2D grid.",
    "input": "grid=[[1,1,0],[0,1,0],[1,0,1]]",
    "output": "3",
    "solution": """# DFS Solution"""
},

{
    "title": "Course Schedule",
    "difficulty": "Medium",
    "topic": "Graph, Topological Sort",
    "description": "Determine if it is possible to finish all courses.",
    "input": "numCourses=2, prerequisites=[[1,0]]",
    "output": "True",
    "solution": """# Topological Sort (Kahn's Algorithm)"""
},
{
    "title": "Kth Largest Element in an Array",
    "difficulty": "Medium",
    "topic": "Heap",
    "description": "Find the kth largest element in an unsorted array.",
    "input": "nums=[3,2,1,5,6,4], k=2",
    "output": "5",
    "solution": """import heapq

def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]"""
},

{
    "title": "Merge K Sorted Lists",
    "difficulty": "Hard",
    "topic": "Linked List, Heap",
    "description": "Merge k sorted linked lists into one sorted linked list.",
    "input": "lists=[[1,4,5],[1,3,4],[2,6]]",
    "output": "[1,1,2,3,4,4,5,6]",
    "solution": """# Use Min Heap to merge k sorted linked lists efficiently."""
},

{
    "title": "Trapping Rain Water",
    "difficulty": "Hard",
    "topic": "Two Pointers",
    "description": "Compute how much rain water can be trapped between the bars.",
    "input": "[0,1,0,2,1,0,1,3,2,1,2,1]",
    "output": "6",
    "solution": """def trap(height):
    left,right=0,len(height)-1
    leftMax=rightMax=0
    water=0

    while left<right:

        if height[left]<height[right]:

            if height[left]>=leftMax:
                leftMax=height[left]
            else:
                water+=leftMax-height[left]

            left+=1

        else:

            if height[right]>=rightMax:
                rightMax=height[right]
            else:
                water+=rightMax-height[right]

            right-=1

    return water"""
},

{
    "title": "Word Ladder",
    "difficulty": "Hard",
    "topic": "Graph, BFS",
    "description": "Find the length of the shortest transformation sequence from beginWord to endWord.",
    "input": 'beginWord="hit", endWord="cog"',
    "output": "5",
    "solution": """# Breadth First Search Solution"""
},

{
    "title": "Median of Two Sorted Arrays",
    "difficulty": "Hard",
    "topic": "Binary Search",
    "description": "Find the median of two sorted arrays in O(log(min(n,m))).",
    "input": "nums1=[1,3], nums2=[2]",
    "output": "2.0",
    "solution": """# Binary Search Partition Method"""
},

{
    "title": "LRU Cache",
    "difficulty": "Hard",
    "topic": "Design",
    "description": "Design an LRU Cache supporting get() and put() in O(1).",
    "input": "capacity=2",
    "output": "Cache operations",
    "solution": """from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity=capacity
        self.cache=OrderedDict()

    def get(self,key):

        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self,key,value):

        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key]=value

        if len(self.cache)>self.capacity:
            self.cache.popitem(last=False)"""
},
{
    "title": "N-Queens",
    "difficulty": "Hard",
    "topic": "Backtracking",
    "description": "Place N queens on an N×N chessboard so that no two queens attack each other.",
    "input": "n = 4",
    "output": "[['.Q..','...Q','Q...','..Q.'],['..Q.','Q...','...Q','.Q..']]",
    "solution": """# Backtracking Solution"""
},

{
    "title": "Sudoku Solver",
    "difficulty": "Hard",
    "topic": "Backtracking",
    "description": "Solve a Sudoku puzzle by filling the empty cells.",
    "input": "9 x 9 Sudoku Board",
    "output": "Solved Sudoku",
    "solution": """# Backtracking + DFS"""
},

{
    "title": "Serialize and Deserialize Binary Tree",
    "difficulty": "Hard",
    "topic": "Binary Tree",
    "description": "Design an algorithm to serialize and deserialize a binary tree.",
    "input": "[1,2,3,null,null,4,5]",
    "output": "[1,2,3,null,null,4,5]",
    "solution": """# BFS / DFS Serialization"""
},

{
    "title": "Alien Dictionary",
    "difficulty": "Hard",
    "topic": "Graph",
    "description": "Determine the order of characters in an alien language using a sorted dictionary.",
    "input": '["wrt","wrf","er","ett","rftt"]',
    "output": '"wertf"',
    "solution": """# Topological Sort"""
},

{
    "title": "Minimum Window Substring",
    "difficulty": "Hard",
    "topic": "Sliding Window",
    "description": "Find the minimum window substring that contains all characters of another string.",
    "input": 's="ADOBECODEBANC", t="ABC"',
    "output": '"BANC"',
    "solution": """# Sliding Window"""
},

{
    "title": "Regular Expression Matching",
    "difficulty": "Hard",
    "topic": "Dynamic Programming",
    "description": "Implement regular expression matching with support for '.' and '*'.",
    "input": 's="aab", p="c*a*b"',
    "output": "True",
    "solution": """# Dynamic Programming"""
}


]