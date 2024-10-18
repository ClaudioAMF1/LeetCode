# LeetCode Solutions Repository

Welcome to my LeetCode Solutions repository! 🎯 This repository contains solutions to various problems from LeetCode, written in multiple programming languages. It serves as a personal archive of my problem-solving journey and a reference for others looking to understand different approaches to solving coding challenges.

## 🗂️ Repository Structure

The repository is organized by problem categories and difficulty levels, following the structure below:

```markdown
├── Easy/
├── Medium/
├── Hard/
├── README.md
└── Languages/
    ├── Python/
    ├── Java/
    ├── C++/
    └── OtherLanguages/
```


- **Easy/**: Solutions to problems classified as "Easy" on LeetCode.
- **Medium/**: Solutions to problems classified as "Medium" on LeetCode.
- **Hard/**: Solutions to problems classified as "Hard" on LeetCode.
- **Languages/**: Organizes solutions by programming language (e.g., Python, Java, C++, etc.).

## 🚀 How to Use

Each problem solution is stored in its corresponding folder based on the difficulty level. The solution files are named according to the problem's name or ID from LeetCode, and they contain the problem description, approach, and solution.

For example:

```markdown
├── Easy
  ├── Two_Sum.py
  ├── Palindrome_Number.java
   └── Reverse_Integer.cpp
```


1. Clone the repository:
```bash
   git clone https://github.com/ClaudioAMF1/LeetCode
```

2. Navigate to the folder corresponding to the problem:
```bash
   cd LeetCode
```

3. Run the solution in your local environment using your preferred compiler or interpreter. For example, for Python:
```bash
python3 Two_Sum.py
```

## 👇🏼 Solution Format

Each solution follows this basic format:

- **Problem Title**: The name of the problem.
- **Problem Link**: Link to the problem on LeetCode.
- **Approach**: Explanation of the approach used to solve the problem.
- **Complexity Analysis**: Time and space complexity analysis of the solution.
- **Code**: The implementation of the solution in the chosen language.

### Example
```bash
# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/

# Approach:
# - Use a hash map to store the complement of each number as we iterate through the array.
# - If the complement is found in the hash map, return the indices.

# Complexity Analysis:
# - Time: O(n), where n is the number of elements in the array.
# - Space: O(n), due to the use of the hash map to store the elements.

def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
```

---
