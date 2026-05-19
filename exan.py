import collections
import itertools
from typing import Optional, List

# Bağlı Liste (Linked List) Düğüm Tanımı (Sistemde zaten tanımlıdır, bilgi amaçlıdır)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
#-----------------------------------
    # 1. 217. Contains Duplicate
#-----------------------------------
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
#-----------------------------------
    # 2. 242. Valid Anagram
#-----------------------------------
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return collections.Counter(s) == collections.Counter(t)

#-----------------------------------
    # 3. 1. Two Sum
#-----------------------------------
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target - num], i]
            num_map[num] = i
        return []

    #-----------------------------------
    # 5. 125. Valid Palindrome
    #-----------------------------------
    
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum(): left += 1
            while left < right and not s[right].isalnum(): right -= 1
            if s[left].lower() != s[right].lower(): return False
            left += 1; right -= 1
        return True

#-----------------------------------
    # 6. 167. Two Sum II - Input Array Is Sorted
#-----------------------------------
    def twoSumII(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target: return [left + 1, right + 1]
            elif curr_sum < target: left += 1
            else: right -= 1
        return []

#-----------------------------------
    # 7. 121. Best Time to Buy and Sell Stock
#-----------------------------------
    
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = float('inf'), 0
        for price in prices:
            if price < min_price: min_price = price
            elif price - min_price > max_profit: max_profit = price - min_price
        return max_profit

#-----------------------------------
    # 8. 3. Longest Substring Without Repeating Characters
#-----------------------------------
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx = {}
        max_len = left = 0
        for right, char in enumerate(s):
            if char in char_idx and char_idx[char] >= left:
                left = char_idx[char] + 1
            char_idx[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len

#-----------------------------------
    # 9. 206. Reverse Linked List
#-----------------------------------
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

#-----------------------------------
    # 10. 21. Merge Two Sorted Lists
#-----------------------------------
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode(-1)
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next

#-----------------------------------
    # 11. 141. Linked List Cycle
#-----------------------------------
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast: return True
        return False

#-----------------------------------
    # 12. 19. Remove Nth Node From End of List
#-----------------------------------
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n + 1): fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next

#-----------------------------------
    # 13. 20. Valid Parentheses
#-----------------------------------
    
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top: return False
            else:
                stack.append(char)
        return not stack

#-----------------------------------
# 4. 303. Range Sum Query - Immutable (Ayrı Sınıf)
#-----------------------------------

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = list(itertools.accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

#-----------------------------------
# 14. 155. Min Stack (Ayrı Sınıf)
#-----------------------------------

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, curr_min))

    def pop(self) -> None: self.stack.pop()
    def top(self) -> int: return self.stack[-1][0]
    def getMin(self) -> int: return self.stack[-1][1]
