java_questions = [

    {
        "title": "Two Sum",
        "topic": "Arrays",
        "difficulty": "Medium",
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
        "input": "nums = [2,7,11,15]\ntarget = 9",
        "output": "[0,1]",
        "solution": """class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<>();

        for(int i=0;i<nums.length;i++){

            int diff = target - nums[i];

            if(map.containsKey(diff))
                return new int[]{map.get(diff), i};

            map.put(nums[i], i);
        }

        return new int[]{};
    }
}"""
    },

    {
        "title": "Reverse String",
        "topic": "Strings",
        "difficulty": "Easy",
        "description": "Reverse a given string.",
        "input": "Hello",
        "output": "olleH",
        "solution": """public class Main{

    public static void main(String[] args){

        String s="Hello";

        String rev="";

        for(int i=s.length()-1;i>=0;i--){

            rev+=s.charAt(i);

        }

        System.out.println(rev);

    }

}"""
    },

    {
        "title": "Palindrome Number",
        "topic": "Math",
        "difficulty": "Easy",
        "description": "Check whether a number is palindrome.",
        "input": "121",
        "output": "true",
        "solution": """class Solution{

    public boolean isPalindrome(int x){

        String s=x+"";

        return s.equals(
        new StringBuilder(s).reverse().toString());

    }

}"""
    },

    {
        "title": "Valid Parentheses",
        "topic": "Stack",
        "difficulty": "Medium",
        "description": "Determine whether the brackets are balanced.",
        "input": "()[]{}",
        "output": "true",
        "solution": """class Solution{

    public boolean isValid(String s){

        Stack<Character> st=new Stack<>();

        for(char c:s.toCharArray()){

            if(c=='(')
                st.push(')');

            else if(c=='{')
                st.push('}');

            else if(c=='[')
                st.push(']');

            else{

                if(st.isEmpty()||st.pop()!=c)
                    return false;

            }

        }

        return st.isEmpty();

    }

}"""
    },

    {
        "title": "Maximum Subarray",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "description": "Find maximum subarray sum.",
        "input": "[-2,1,-3,4,-1,2,1,-5,4]",
        "output": "6",
        "solution": """class Solution{

    public int maxSubArray(int[] nums){

        int max=nums[0];

        int cur=0;

        for(int n:nums){

            cur=Math.max(n,cur+n);

            max=Math.max(max,cur);

        }

        return max;

    }

}"""
    },

    {
        "title": "Binary Search",
        "topic": "Searching",
        "difficulty": "Easy",
        "description": "Find target using Binary Search.",
        "input": "[1,2,3,4,5], target=4",
        "output": "3",
        "solution": """class Solution{

    public int search(int[] nums,int target){

        int l=0,r=nums.length-1;

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

    }

}"""
    },
    {
        "title": "Merge Sorted Arrays",
        "topic": "Arrays",
        "difficulty": "Medium",
        "description": "Merge two sorted arrays.",
        "input": "[1,2,4] [1,3,4]",
        "output": "[1,1,2,3,4,4]",
        "solution": """import java.util.Arrays;

public class Main{

    public static void main(String[] args){

        int[] a={1,2,4};
        int[] b={1,3,4};

        int[] c=new int[a.length+b.length];

        System.arraycopy(a,0,c,0,a.length);
        System.arraycopy(b,0,c,a.length,b.length);

        Arrays.sort(c);

        System.out.println(Arrays.toString(c));

    }

}"""
    },

    {
        "title":"Longest Common Prefix",
        "topic":"Strings",
        "difficulty":"Medium",
        "description":"Find longest common prefix.",
        "input":"flower flow flight",
        "output":"fl",
        "solution":"""class Solution{

    public String longestCommonPrefix(String[] strs){

        String pre=strs[0];

        for(String s:strs){

            while(!s.startsWith(pre))
                pre=pre.substring(0,pre.length()-1);

        }

        return pre;

    }

}"""
    },

    {
        "title":"Product of Array Except Self",
        "topic":"Arrays",
        "difficulty":"Medium",
        "description":"Return product except self.",
        "input":"[1,2,3,4]",
        "output":"[24,12,8,6]",
        "solution":"""class Solution{

    public int[] productExceptSelf(int[] nums){

        int n=nums.length;

        int[] ans=new int[n];

        ans[0]=1;

        for(int i=1;i<n;i++)
            ans[i]=ans[i-1]*nums[i-1];

        int right=1;

        for(int i=n-1;i>=0;i--){

            ans[i]*=right;

            right*=nums[i];

        }

        return ans;

    }

}"""
    },

    {
        "title":"Container With Most Water",
        "topic":"Two Pointers",
        "difficulty":"Medium",
        "description":"Find maximum water container.",
        "input":"[1,8,6,2,5,4,8,3,7]",
        "output":"49",
        "solution":"""class Solution{

    public int maxArea(int[] h){

        int l=0,r=h.length-1;

        int ans=0;

        while(l<r){

            ans=Math.max(ans,
            Math.min(h[l],h[r])*(r-l));

            if(h[l]<h[r]) l++;

            else r--;

        }

        return ans;

    }

}"""
    },

    {
        "title":"Longest Consecutive Sequence",
        "topic":"HashSet",
        "difficulty":"Hard",
        "description":"Find longest consecutive sequence.",
        "input":"[100,4,200,1,3,2]",
        "output":"4",
        "solution":"""class Solution{

    public int longestConsecutive(int[] nums){

        HashSet<Integer> set=new HashSet<>();

        for(int n:nums)
            set.add(n);

        int best=0;

        for(int n:set){

            if(!set.contains(n-1)){

                int cur=n;

                int len=1;

                while(set.contains(cur+1)){

                    cur++;

                    len++;

                }

                best=Math.max(best,len);

            }

        }

        return best;

    }

}"""
    },

    {
        "title":"Find Duplicate Number",
        "topic":"Arrays",
        "difficulty":"Medium",
        "description":"Find duplicate number.",
        "input":"[1,3,4,2,2]",
        "output":"2",
        "solution":"""class Solution{

    public int findDuplicate(int[] nums){

        HashSet<Integer> set=new HashSet<>();

        for(int n:nums){

            if(set.contains(n))
                return n;

            set.add(n);

        }

        return -1;

    }

}"""
    },

    {
        "title":"Top K Frequent Elements",
        "topic":"Heap",
        "difficulty":"Hard",
        "description":"Find top k frequent elements.",
        "input":"nums=[1,1,1,2,2,3], k=2",
        "output":"[1,2]",
        "solution":"""class Solution{

    public int[] topKFrequent(int[] nums,int k){

        HashMap<Integer,Integer> map=new HashMap<>();

        for(int n:nums)
            map.put(n,map.getOrDefault(n,0)+1);

        PriorityQueue<Integer> pq=
        new PriorityQueue<>((a,b)->map.get(b)-map.get(a));

        pq.addAll(map.keySet());

        int[] ans=new int[k];

        for(int i=0;i<k;i++)
            ans[i]=pq.poll();

        return ans;

    }

}"""
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
        "description":"Find all triplets whose sum is zero.",
        "input":"[-1,0,1,2,-1,-4]",
        "output":"[[-1,-1,2],[-1,0,1]]",
        "solution":"""// Two Pointer Solution"""
    },
        {
        "title":"Group Anagrams",
        "topic":"HashMap",
        "difficulty":"Hard",
        "description":"Group all anagrams together.",
        "input":"eat tea ate tan nat",
        "output":"[[eat,tea,ate],[tan,nat]]",
        "solution":"""// HashMap<String,List<String>> Solution"""
    },

    {
        "title":"Number of Islands",
        "topic":"Graphs",
        "difficulty":"Hard",
        "description":"Count the number of islands in a grid.",
        "input":"Grid",
        "output":"3",
        "solution":"""// DFS Solution"""
    },

    {
        "title":"Course Schedule",
        "topic":"Graphs",
        "difficulty":"Hard",
        "description":"Check whether all courses can be completed.",
        "input":"numCourses=2",
        "output":"true",
        "solution":"""// Topological Sort"""
    },

    {
        "title":"Kth Largest Element",
        "topic":"Heap",
        "difficulty":"Hard",
        "description":"Find kth largest element in an array.",
        "input":"[3,2,1,5,6,4], k=2",
        "output":"5",
        "solution":"""// PriorityQueue Solution"""
    },

    {
        "title":"Merge K Sorted Lists",
        "topic":"Linked List",
        "difficulty":"Hard",
        "description":"Merge k sorted linked lists.",
        "input":"[[1,4,5],[1,3,4],[2,6]]",
        "output":"Merged List",
        "solution":"""// Priority Queue Solution"""
    },

    {
        "title":"Trapping Rain Water",
        "topic":"Two Pointers",
        "difficulty":"Hard",
        "description":"Calculate trapped rain water.",
        "input":"[0,1,0,2,1,0,1,3]",
        "output":"6",
        "solution":"""// Two Pointer Solution"""
    },

    {
        "title":"Word Ladder",
        "topic":"Graphs",
        "difficulty":"Hard",
        "description":"Find shortest transformation sequence.",
        "input":"hit -> cog",
        "output":"5",
        "solution":"""// BFS Solution"""
    },

    {
        "title":"Median of Two Sorted Arrays",
        "topic":"Binary Search",
        "difficulty":"Hard",
        "description":"Find median of two sorted arrays.",
        "input":"[1,3] [2]",
        "output":"2.0",
        "solution":"""// Binary Search Solution"""
    },
        {
        "title":"LRU Cache",
        "topic":"Design",
        "difficulty":"Hard",
        "description":"Design an LRU Cache data structure.",
        "input":"capacity = 2",
        "output":"Cache Operations",
        "solution":"""// LinkedHashMap Solution"""
    },

    {
        "title":"N Queens",
        "topic":"Backtracking",
        "difficulty":"Hard",
        "description":"Place N queens on an N×N chessboard.",
        "input":"n = 4",
        "output":"2 Solutions",
        "solution":"""// Backtracking Solution"""
    },

    {
        "title":"Sudoku Solver",
        "topic":"Backtracking",
        "difficulty":"Hard",
        "description":"Solve the given Sudoku board.",
        "input":"9 x 9 Sudoku",
        "output":"Solved Sudoku",
        "solution":"""// DFS + Backtracking"""
    },

    {
        "title":"Serialize Binary Tree",
        "topic":"Trees",
        "difficulty":"Hard",
        "description":"Serialize and Deserialize a Binary Tree.",
        "input":"Binary Tree",
        "output":"Serialized Tree",
        "solution":"""// BFS / DFS Solution"""
    },

    {
        "title":"Alien Dictionary",
        "topic":"Graphs",
        "difficulty":"Hard",
        "description":"Find the order of characters in an alien language.",
        "input":"['wrt','wrf','er','ett','rftt']",
        "output":"wertf",
        "solution":"""// Topological Sort"""
    },

    {
        "title":"Minimum Window Substring",
        "topic":"Sliding Window",
        "difficulty":"Hard",
        "description":"Find the smallest window containing all characters.",
        "input":"ADOBECODEBANC",
        "output":"BANC",
        "solution":"""// Sliding Window"""
    },

    {
        "title":"Regular Expression Matching",
        "topic":"Dynamic Programming",
        "difficulty":"Hard",
        "description":"Implement regex matching using '.' and '*'.",
        "input":"aab",
        "output":"true",
        "solution":"""// Dynamic Programming"""
    }


]