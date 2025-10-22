# 🚀 CodeEveryday — My Road to DSA Mastery

Welcome to my **#CodeEveryday-DSA** repository!  
Here, I document my daily progress in mastering **Data Structures and Algorithms** — one problem at a time 💻🔥  

---

## 📅 Daily Progress

### 🧩 Day 1 — Stack and Queue
- **Languages:** Python 🐍  
- **Concepts Used:** Stack, Queue, Implementation using each other  
- **Files:**
  - [Stack_using_Queue.py](./Day1_Stack_and_Queue/Stack_using_Queue.py)
  - [Queue_using_Stack.py](./Day1_Stack_and_Queue/Queue_using_Stack.py)
- **What I Learned:**
  - How to simulate **stack operations using a queue**.  
  - How to build a **queue using stacks**.  
  - Understanding **data structure interdependence**.  

---

### 🧩 Day 2 — Next Greater Element II
- **Languages:** Python 🐍 | Java ☕  
- **Concepts Used:** Stack, Monotonic Stack, Circular Array, Binary Search  
- **Problem Link:** [LeetCode - Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
- **My Solutions:**
  - [NextGreaterElementII.py](./Day2_Next_Greater_Element_II/NextGreaterElementII.py)
  - [NextGreaterElementII.java](./Day2_Next_Greater_Element_II/NextGreaterElementII.java)
- **What I Learned:**
  - How to handle **circular arrays** efficiently.  
  - Using a **stack** to find next greater elements.  
  - Applied **binary search** for additional optimization.
   

---
## 🗓️ Day 3 — Sum of Subarray Minimums
**Problem Solved:** Sum of Subarray Minimums  
**Concepts:** Monotonic Stack, Subarray Contribution, Modulo Arithmetic  
**Languages:** Python, Java  
**Link:** [Day3_Sum_of_Subarray_Minimums](./Day3_Sum_of_Subarray_Minimums)  
**What I Learned:**
- How every element contributes as minimum in some subarrays by counting how far left and right it can extend.
- Use a monotonic increasing stack to compute those extents in O(n).
- Handle very large sums and mod `10^9 + 7`.

## 🗓️ Day 4 — Remove K Digits
**Problem Solved:** 402. Remove K Digits  
**Concepts:** Monotonic Stack, Greedy Approach, String Manipulation  
**Languages:** Python, Java  
**Link:** [Day4_Remove_K_Digits](./Day4_Remove_K_Digits)  
**What I Learned:**
- Used a monotonic increasing stack to remove digits greedily and form the smallest number.
- Ensured no leading zeros in the resulting number.
- If `k` remained after traversal, removed digits from the end of the stack.
- Learned how greedy logic combined with stack operations achieves an optimal O(n) solution.

---

## 🗓️ Day 5 — Asteroid Collision
**Problem Solved:** 735. Asteroid Collision  
**Concepts:** Stack Simulation, Sign-Based Collisions, Iterative Elimination  
**Languages:** Python  
**Link:** [Day5_Asteroid_Collision](./Day5_Asteroid_Collision)  
**What I Learned:**
- Used a stack to simulate asteroid motion and handle collisions efficiently.
- Compared directions using sign (+ → right, − → left) to detect collisions.
- Managed multiple collisions using nested popping logic until stability was achieved.
- Strengthened understanding of stack-based simulation problems.


# 🚀 Day 6 – Binary Subarrays With Sum

**Problem:**  
Given a binary array `nums` and an integer `goal`, return the number of non-empty subarrays with a sum equal to `goal`.

📘 **LeetCode Link:** [Binary Subarrays With Sum (#930)](https://leetcode.com/problems/binary-subarrays-with-sum/)

---

## 💡 Approach

We use the **two-pointer sliding window technique** to count:
1. Subarrays with sum ≤ goal  
2. Subarrays with sum ≤ goal−1  
The difference between these two gives the exact number of subarrays with sum = goal.

---

## 🧠 Intuition
Instead of recalculating sums repeatedly, we maintain a window that expands and shrinks based on the number of 1s encountered.

---

## 🧮 Time Complexity
- **O(n)** – Single traversal using two pointers  
- **O(1)** – Constant extra space


---



## 🗓️ Day 7 — Number of Substrings Containing All Three Characters
**Problem Solved:** Number of Substrings Containing All Three Characters  
**Concepts:** Sliding Window, HashMap, Substring Counting  
**Languages:** Python, Java  
**Link:** [Day7_Number_of_Substrings_Containing_All_Three_Characters](./Day7_Number_of_Substrings_Containing_All_Three_Characters)  
**What I Learned:**
- Applied **sliding window** with two pointers and frequency tracking.  
- Used the formula `count(at most k) - count(at most k-1)` to find substrings with exactly 3 distinct characters.  
- Optimized brute-force substring checking from **O(n²)** to **O(n)**.  
- Strengthened understanding of **window shrinking and character frequency management**.

---

## 🗓️ Day 8 — Subarrays with K Distinct Integers
**Problem Solved:** Subarrays with K Distinct Integers  
**Concepts:** Sliding Window, HashMap / Frequency Map, Two Pointer Technique  
**Languages:** Python, Java  
**Link:** [Day8_Subarrays_With_K_Distinct_Integers](./Day8_Subarrays_With_K_Distinct_Integers)  

**What I Learned:**
- Solved using the idea:  
  `count(at most K distinct) - count(at most (K-1) distinct) = count(exactly K distinct)`  
- Maintained a dynamic window and adjusted `p2` when unique elements exceeded `k`.  
- Used HashMap / Dictionary to efficiently track element counts within O(n) time.  
- Strengthened understanding of sliding window logic for frequency-based problems.

---

## 🗓️ Day 9 — Count Number of Nice Subarrays
**Problem Solved:** Count Number of Nice Subarrays  
**Concepts:** Sliding Window, Two Pointers, Subarray Counting  
**Languages:** Python, Java  
**Link:** [Day9_Count_Number_of_Nice_Subarrays](./Day9_Count_Number_of_Nice_Subarrays)  

**What I Learned:**
- How to count subarrays with *exactly K* odd numbers using the difference of two “at most K” subarray counts.  
- Sliding window efficiently maintains dynamic ranges that meet the condition.  
- Key formula:  
---


# 🚀 Day 10: Combination Sum

## Problem
Given an array of distinct integers `candidates` and a target integer `target`, return all unique combinations of `candidates` where the chosen numbers sum to `target`. The same number may be chosen multiple times.

## Approach
- Used recursion and backtracking to generate all valid combinations.
- If the current sum equals the target → store the current list.
- If it exceeds → backtrack.
- Continue exploring both include/exclude paths.

---

🗓️ Day 11 — Combination Sum II

Problem Solved: Combination Sum II
Concepts: Backtracking, Recursion, Sorting, Duplicate Handling
Languages: Python, Java
Link: Day11_Combination_Sum_II

What I Learned:

Used sorting and skipping duplicates to avoid generating the same combination twice.

Improved pruning logic by stopping early when the current candidate exceeds the target.

Understood the difference between Combination Sum I (reuse allowed) and Combination Sum II (each number used once).

Gained deeper insight into recursive search tree optimization.

---


## 🗓️ Day 12 — Word Search
**Problem Solved:** Word Search (LeetCode #79)  
**Concepts:** DFS, Backtracking, Matrix Traversal, Recursion  
**Languages:** Python  
**Link:** [Day12_Word_Search](./Day12_Word_Search)  

**What I Learned:**
- Implemented a depth-first search (DFS) with backtracking to explore all possible paths.  
- Learned how to efficiently track visited cells using a set to avoid revisiting.  
- Handled boundary conditions and recursion termination carefully.  
- Improved problem-solving skills for grid-based word traversal challenges.

---

### 💡 My Goal
> Solve one DSA problem every day — no excuses, just consistency.  

---

### 🏁 Follow My Journey
📂 Repository: [CodeEveryday-DSA](https://github.com/chikkuduchandu/CodeEveryday-DSA)
