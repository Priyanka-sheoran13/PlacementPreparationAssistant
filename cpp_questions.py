cpp_questions = [

    {
        "title":"Two Sum",
        "topic":"Arrays",
        "difficulty":"Medium",
        "description":"Given an integer array nums and an integer target, return indices of the two numbers such that they add up to target.",
        "input":"nums = [2,7,11,15]\ntarget = 9",
        "output":"[0,1]",
        "solution":"""#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

vector<int> twoSum(vector<int>& nums,int target){

    unordered_map<int,int> mp;

    for(int i=0;i<nums.size();i++){

        int diff=target-nums[i];

        if(mp.count(diff))
            return {mp[diff],i};

        mp[nums[i]]=i;
    }

    return {};
}"""
    },

    {
        "title":"Reverse String",
        "topic":"Strings",
        "difficulty":"Easy",
        "description":"Reverse the given string.",
        "input":"Hello",
        "output":"olleH",
        "solution":"""#include<iostream>
#include<algorithm>
using namespace std;

int main(){

    string s="Hello";

    reverse(s.begin(),s.end());

    cout<<s;

}"""
    },

    {
        "title":"Palindrome Number",
        "topic":"Math",
        "difficulty":"Easy",
        "description":"Check whether a number is palindrome.",
        "input":"121",
        "output":"true",
        "solution":"""#include<iostream>
using namespace std;

int main(){

    int n=121;

    int temp=n;

    int rev=0;

    while(n){

        rev=rev*10+n%10;

        n/=10;

    }

    if(temp==rev)

        cout<<"True";

    else

        cout<<"False";

}"""
    },

    {
        "title":"Valid Parentheses",
        "topic":"Stack",
        "difficulty":"Medium",
        "description":"Determine whether the brackets are balanced.",
        "input":"()[]{}",
        "output":"true",
        "solution":"""#include<iostream>
#include<stack>
using namespace std;

bool valid(string s){

    stack<char> st;

    for(char c:s){

        if(c=='(')
            st.push(')');

        else if(c=='[')
            st.push(']');

        else if(c=='{')
            st.push('}');

        else{

            if(st.empty() || st.top()!=c)
                return false;

            st.pop();

        }

    }

    return st.empty();

}"""
    },

    {
        "title":"Maximum Subarray",
        "topic":"Dynamic Programming",
        "difficulty":"Medium",
        "description":"Find maximum subarray sum.",
        "input":"[-2,1,-3,4,-1,2,1,-5,4]",
        "output":"6",
        "solution":"""#include<iostream>
#include<vector>
using namespace std;

int maxSubArray(vector<int>& nums){

    int best=nums[0];

    int cur=0;

    for(int x:nums){

        cur=max(x,cur+x);

        best=max(best,cur);

    }

    return best;

}"""
    },

    {
        "title":"Binary Search",
        "topic":"Searching",
        "difficulty":"Easy",
        "description":"Find target using Binary Search.",
        "input":"[1,2,3,4,5], target=4",
        "output":"3",
        "solution":"""#include<iostream>
#include<vector>
using namespace std;

int search(vector<int>& nums,int target){

    int l=0,r=nums.size()-1;

    while(l<=r){

        int m=(l+r)/2;

        if(nums[m]==target)
            return m;

        if(nums[m]<target)
            l=m+1;

        else
            r=m-1;

    }

    return -1;

}"""
    },
    {
        "title":"Merge Sorted Arrays",
        "topic":"Arrays",
        "difficulty":"Medium",
        "description":"Merge two sorted arrays into one sorted array.",
        "input":"[1,2,4] [1,3,4]",
        "output":"[1,1,2,3,4,4]",
        "solution":"""#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){

    vector<int> a={1,2,4};
    vector<int> b={1,3,4};

    a.insert(a.end(),b.begin(),b.end());

    sort(a.begin(),a.end());

    for(int x:a)
        cout<<x<<" ";

}"""
    },

    {
        "title":"Longest Common Prefix",
        "topic":"Strings",
        "difficulty":"Medium",
        "description":"Find the longest common prefix among strings.",
        "input":"flower flow flight",
        "output":"fl",
        "solution":"""class Solution{
public:
string longestCommonPrefix(vector<string>& strs){

    string pre=strs[0];

    for(string s:strs){

        while(s.find(pre)!=0)
            pre.pop_back();

    }

    return pre;
}
};"""
    },

    {
        "title":"Product of Array Except Self",
        "topic":"Arrays",
        "difficulty":"Medium",
        "description":"Return product of array except self.",
        "input":"[1,2,3,4]",
        "output":"[24,12,8,6]",
        "solution":"""class Solution{
public:

vector<int> productExceptSelf(vector<int>& nums){

    int n=nums.size();

    vector<int> ans(n,1);

    for(int i=1;i<n;i++)
        ans[i]=ans[i-1]*nums[i-1];

    int right=1;

    for(int i=n-1;i>=0;i--){

        ans[i]*=right;

        right*=nums[i];

    }

    return ans;

}
};"""
    },

    {
        "title":"Container With Most Water",
        "topic":"Two Pointers",
        "difficulty":"Medium",
        "description":"Find maximum amount of water.",
        "input":"[1,8,6,2,5,4,8,3,7]",
        "output":"49",
        "solution":"""class Solution{
public:

int maxArea(vector<int>& h){

    int l=0,r=h.size()-1;

    int ans=0;

    while(l<r){

        ans=max(ans,min(h[l],h[r])*(r-l));

        if(h[l]<h[r])
            l++;
        else
            r--;

    }

    return ans;

}
};"""
    },

    {
        "title":"Longest Consecutive Sequence",
        "topic":"Hash Set",
        "difficulty":"Hard",
        "description":"Find the longest consecutive sequence.",
        "input":"[100,4,200,1,3,2]",
        "output":"4",
        "solution":"""class Solution{
public:

int longestConsecutive(vector<int>& nums){

    unordered_set<int> st(nums.begin(),nums.end());

    int best=0;

    for(int n:st){

        if(!st.count(n-1)){

            int cur=n;

            int len=1;

            while(st.count(cur+1)){

                cur++;

                len++;

            }

            best=max(best,len);

        }

    }

    return best;

}
};"""
    },

    {
        "title":"Find Duplicate Number",
        "topic":"Arrays",
        "difficulty":"Medium",
        "description":"Find duplicate element.",
        "input":"[1,3,4,2,2]",
        "output":"2",
        "solution":"""class Solution{
public:

int findDuplicate(vector<int>& nums){

    unordered_set<int> st;

    for(int x:nums){

        if(st.count(x))
            return x;

        st.insert(x);

    }

    return -1;

}
};"""
    },

    {
        "title":"Top K Frequent Elements",
        "topic":"Heap",
        "difficulty":"Hard",
        "description":"Return k most frequent elements.",
        "input":"[1,1,1,2,2,3], k=2",
        "output":"[1,2]",
        "solution":"""// Priority Queue + HashMap Solution"""
    },

    {
        "title":"Search in Rotated Sorted Array",
        "topic":"Binary Search",
        "difficulty":"Hard",
        "description":"Search target in rotated sorted array.",
        "input":"[4,5,6,7,0,1,2]",
        "output":"4",
        "solution":"""// Binary Search Solution"""
    },

    {
        "title":"3 Sum",
        "topic":"Two Pointers",
        "difficulty":"Hard",
        "description":"Find all unique triplets with sum = 0.",
        "input":"[-1,0,1,2,-1,-4]",
        "output":"[[-1,-1,2],[-1,0,1]]",
        "solution":"""// Sorting + Two Pointer Solution"""
    },
        {
        "title":"Group Anagrams",
        "topic":"Hash Map",
        "difficulty":"Hard",
        "description":"Group all anagrams together.",
        "input":"eat tea ate tan nat",
        "output":"[[eat,tea,ate],[tan,nat]]",
        "solution":"""// HashMap<string, vector<string>> Solution"""
    },

    {
        "title":"Number of Islands",
        "topic":"Graphs",
        "difficulty":"Hard",
        "description":"Count the number of islands in a grid.",
        "input":"Grid[][]",
        "output":"3",
        "solution":"""// DFS Solution"""
    },

    {
        "title":"Course Schedule",
        "topic":"Graphs",
        "difficulty":"Hard",
        "description":"Determine if all courses can be completed.",
        "input":"numCourses = 2",
        "output":"true",
        "solution":"""// Topological Sort (Kahn's Algorithm)"""
    },

    {
        "title":"Kth Largest Element",
        "topic":"Heap",
        "difficulty":"Hard",
        "description":"Find the kth largest element in an array.",
        "input":"[3,2,1,5,6,4], k = 2",
        "output":"5",
        "solution":"""// Priority Queue (Min Heap) Solution"""
    },

    {
        "title":"Merge K Sorted Lists",
        "topic":"Linked List",
        "difficulty":"Hard",
        "description":"Merge k sorted linked lists into one sorted list.",
        "input":"[[1,4,5],[1,3,4],[2,6]]",
        "output":"Merged Linked List",
        "solution":"""// Priority Queue Solution"""
    },

    {
        "title":"Trapping Rain Water",
        "topic":"Two Pointers",
        "difficulty":"Hard",
        "description":"Calculate how much rain water can be trapped.",
        "input":"[0,1,0,2,1,0,1,3,2,1,2,1]",
        "output":"6",
        "solution":"""// Two Pointer Solution"""
    },

    {
        "title":"Word Ladder",
        "topic":"Graphs",
        "difficulty":"Hard",
        "description":"Find the shortest transformation sequence.",
        "input":"hit → cog",
        "output":"5",
        "solution":"""// BFS Solution"""
    },

    {
        "title":"Median of Two Sorted Arrays",
        "topic":"Binary Search",
        "difficulty":"Hard",
        "description":"Find the median of two sorted arrays.",
        "input":"[1,3] [2]",
        "output":"2.0",
        "solution":"""// Binary Search Solution"""
    },
        {
        "title":"LRU Cache",
        "topic":"Design",
        "difficulty":"Hard",
        "description":"Design and implement an LRU Cache.",
        "input":"Capacity = 2",
        "output":"Cache Operations",
        "solution":"""// Doubly Linked List + HashMap Solution"""
    },

    {
        "title":"N Queens",
        "topic":"Backtracking",
        "difficulty":"Hard",
        "description":"Place N queens on an N×N chessboard so that no two queens attack each other.",
        "input":"n = 4",
        "output":"2 Solutions",
        "solution":"""// Backtracking Solution"""
    },

    {
        "title":"Sudoku Solver",
        "topic":"Backtracking",
        "difficulty":"Hard",
        "description":"Solve the given Sudoku puzzle.",
        "input":"9 x 9 Sudoku",
        "output":"Solved Sudoku",
        "solution":"""// DFS + Backtracking Solution"""
    },

    {
        "title":"Serialize Binary Tree",
        "topic":"Trees",
        "difficulty":"Hard",
        "description":"Serialize and Deserialize a Binary Tree.",
        "input":"Binary Tree",
        "output":"Serialized String",
        "solution":"""// BFS / DFS Solution"""
    },

    {
        "title":"Alien Dictionary",
        "topic":"Graphs",
        "difficulty":"Hard",
        "description":"Find the order of characters in an alien language.",
        "input":"['wrt','wrf','er','ett','rftt']",
        "output":"wertf",
        "solution":"""// Topological Sort Solution"""
    },

    {
        "title":"Minimum Window Substring",
        "topic":"Sliding Window",
        "difficulty":"Hard",
        "description":"Find the smallest substring containing all characters of another string.",
        "input":"ADOBECODEBANC",
        "output":"BANC",
        "solution":"""// Sliding Window Solution"""
    },

    {
        "title":"Regular Expression Matching",
        "topic":"Dynamic Programming",
        "difficulty":"Hard",
        "description":"Implement regular expression matching using '.' and '*'.",
        "input":"aab",
        "output":"true",
        "solution":"""// Dynamic Programming Solution"""
    }


]