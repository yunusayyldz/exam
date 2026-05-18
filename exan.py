#-------------------------------------------------
# 217. Contains Duplicate
#-------------------------------------------------

#include <vector>
#include <unordered_set>

class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num) > 0) {
                return true; 
            }
            seen.insert(num);
        }
        return false; 
    }
};

#------------------------------------------------
#242. Valid Anagram
#------------------------------------------------

#include <string>
#include <vector>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        std::vector<int> char_counts(26, 0);
        
        for (int i = 0; i < s.length(); ++i) {
            char_counts[s[i] - 'a']++; 
            char_counts[t[i] - 'a']--; 
        }
        
        for (int count : char_counts) {
            if (count != 0) {
                return false; 
            }
        }
        return true;
    }
};

#-----------------------------------------------
# 1. Two Sum
#-----------------------------------------------

#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> num_map;
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (num_map.count(complement) > 0) {
                return {num_map[complement], i};
            }
            num_map[nums[i]] = i;
        }
        return {}; 
    }
};

#-----------------------------------------------
# 303. Range Sum Query - Immutable
#-----------------------------------------------

#include <vector>

class NumArray {
private:
    std::vector<int> prefix; 

public:
    NumArray(std::vector<int>& nums) {
        prefix.resize(nums.size() + 1, 0);
        for (int i = 0; i < nums.size(); ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
    }
    
    int sumRange(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }
};

#------------------------------------------------
# 125. Valid Palindrome
#------------------------------------------------

#include <string>
#include <cctype> 

class Solution {
public:
    bool isPalindrome(std::string s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            while (left < right && !std::isalnum(s[left])) {
                left++;
            }
            while (left < right && !std::isalnum(s[right])) {
                right--;
            }
            if (std::tolower(s[left]) != std::tolower(s[right])) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};

#----------------------------------------------------
# 167. Two Sum II - Input Array Is Sorted
#----------------------------------------------------

#include <vector>
#include <algorithm> 
#include <limits>    

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int min_price = std::numeric_limits<int>::max(); 
        int max_profit = 0;
        
        for (int i = 0; i < prices.size(); ++i) {
            min_price = std::min(min_price, prices[i]);
            max_profit = std::max(max_profit, prices[i] - min_price);
        }
        
        return max_profit;
    }
};

#------------------------------------------------
# 121. Best Time to Buy and Sell Stock
#-----------------------------------------------

#include <vector>
#include <algorithm> 
#include <limits>    

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int min_price = std::numeric_limits<int>::max(); 
        int max_profit = 0;
        
        for (int i = 0; i < prices.size(); ++i) {
            min_price = std::min(min_price, prices[i]);
            max_profit = std::max(max_profit, prices[i] - min_price);
        }
        
        return max_profit;
    }
};

#----------------------------------------------------
# 3. Longest Substring Without Repeating Characters
#----------------------------------------------------

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        std::vector<int> char_index(128, -1);
        int max_length = 0;
        int left = 0; 
        
        for (int right = 0; right < s.length(); ++right) {
            char current_char = s[right];
            
            if (char_index[current_char] >= left) {
                left = char_index[current_char] + 1;
            }
            
            char_index[current_char] = right;
            max_length = std::max(max_length, right - left + 1);
        }
        
        return max_length;
    }
};

#------------------------------------------------------
# 206. Reverse Linked List
#------------------------------------------------------

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            ListNode* next_temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_temp;
        }
        
        return prev;
    }
};

#-----------------------------------------------------
# 21. Merge Two Sorted Lists
#-----------------------------------------------------

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy(-1); 
        ListNode* tail = &dummy;
        
        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }
        
        if (list1 != nullptr) {
            tail->next = list1;
        } else {
            tail->next = list2;
        }
        
        return dummy.next;
    }
};

#-----------------------------------------------------
# 141. Linked List Cycle
#-----------------------------------------------------

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* slow = head; 
        ListNode* fast = head; 
        
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
            
            if (slow == fast) {
                return true; 
            }
        }
        
        return false;
    }
};

#-----------------------------------------------------
# 19. Remove Nth Node From End of List
#-----------------------------------------------------

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0);
        dummy.next = head;
        
        ListNode* slow = &dummy;
        ListNode* fast = &dummy;
        
        for (int i = 0; i <= n; ++i) {
            fast = fast->next;
        }
        
        while (fast != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }
        
        ListNode* nodeToDelete = slow->next;
        slow->next = slow->next->next;
        delete nodeToDelete;
        
        return dummy.next;
    }
};

#-----------------------------------------------------
# 20. Valid Parentheses
#-----------------------------------------------------

#include <string>
#include <stack>

class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> st;
        
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } 
            else {
                if (st.empty()) return false;
                
                char top = st.top();
                if ((c == ')' && top == '(') || 
                    (c == '}' && top == '{') || 
                    (c == ']' && top == '[')) {
                    st.pop();
                } else {
                    return false;
                }
            }
        }
        
        return st.empty();
    }
};

#-----------------------------------------------------
# 155. Min Stack
#-----------------------------------------------------

#include <stack>
#include <algorithm>

class MinStack {
private:
    std::stack<int> main_st;
    std::stack<int> min_st;

public:
    MinStack() {}
    
    void push(int val) {
        main_st.push(val);
        if (min_st.empty() || val <= min_st.top()) {
            min_st.push(val);
        }
    }
    
    void pop() {
        if (main_st.top() == min_st.top()) {
            min_st.pop();
        }
        main_st.pop();
    }
    
    int top() {
        return main_st.top();
    }
    
    int getMin() {
        return min_st.top();
    }
};
