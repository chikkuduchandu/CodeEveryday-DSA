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


### 💡 My Goal
> Solve one DSA problem every day — no excuses, just consistency.  

---

### 🏁 Follow My Journey
📂 Repository: [CodeEveryday-DSA](https://github.com/chikkuduchandu/CodeEveryday-DSA)
