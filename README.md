# Longest Unimodal Subsequence - Dynamic Programming

## Assignment Instructions

Your task is to complete the `unimodal.py` file by filling in the missing dynamic programming logic.

## Problem Description

This program implements a dynamic programming solution to find the **Longest Unimodal Subsequence (LUS)** in a sequence of numbers.

A **unimodal subsequence** is a subsequence that first increases (strictly) and then decreases (strictly), forming a "mountain" or "peak" shape. Formally, a subsequence `a[i₁], a[i₂], ..., a[iₖ]` is unimodal if there exists an index `p` (1 ≤ p ≤ k) such that:
- `a[i₁] < a[i₂] < ... < a[iₚ]` (strictly increasing up to peak)
- `a[iₚ] > a[iₚ₊₁] > ... > a[iₖ]` (strictly decreasing after peak)

**Important:** A unimodal subsequence must have at least one element in both the increasing and decreasing parts, so the minimum length is 3 (up-peak-down).

### Examples

**Example 1:** Sequence `[1, 5, 3, 6, 4, 8, 2]`
- Unimodal subsequence: `[1, 5, 6, 8, 2]` or `[1, 3, 6, 8, 2]` - length **5**
  - Increasing: `1 < 5 < 6 < 8` (or `1 < 3 < 6 < 8`)
  - Decreasing: `8 > 2`

**Example 2:** Sequence `[1, 2, 3, 4, 5]` (only increasing)
- No valid unimodal subsequence (length **0**)
- Reason: No decreasing part

**Example 3:** Sequence `[5, 4, 3, 2, 1]` (only decreasing)
- No valid unimodal subsequence (length **0**)
- Reason: No increasing part

**Example 4:** Sequence `[1, 4, 3, 5, 2]`
- Unimodal subsequence: `[1, 4, 5, 2]` - length **4**
  - Increasing: `1 < 4 < 5`
  - Decreasing: `5 > 2`

## Relationship to Longest Monotone Subsequence (LMS)

This problem builds on the Longest Monotone Subsequence problem from Chapter 4 of the textbook. Recall that for LMS, we define:
- `R[j]` = length of the longest monotone non-decreasing subsequence ending at position `j`

For the unimodal problem, we need **two** dynamic programming arrays:
- `INC[j]` = length of the longest **strictly increasing** subsequence ending at position `j`
- `DEC[j]` = length of the longest **strictly decreasing** subsequence starting at position `j`

## Dynamic Programming Approach

The solution requires computing both arrays and then finding the best "peak":

### Step 1: Compute INC array (left to right)
- `INC[0] = 1` (base case)
- For `j > 0`: `INC[j] = 1 + max{INC[i] | i < j and arr[i] < arr[j]}`
- If no such `i` exists, then `INC[j] = 1`

### Step 2: Compute DEC array (right to left)
- `DEC[n-1] = 1` (base case, where n is array length)
- For `j < n-1`: `DEC[j] = 1 + max{DEC[i] | i > j and arr[j] > arr[i]}`
- If no such `i` exists, then `DEC[j] = 1`

### Step 3: Find the longest unimodal subsequence
For each position `j` that could be a peak:
- If `INC[j] > 1` AND `DEC[j] > 1`, then `j` can be a peak
- The unimodal subsequence length with peak at `j` is: `INC[j] + DEC[j] - 1`
- The answer is: `max{INC[j] + DEC[j] - 1 | INC[j] > 1 and DEC[j] > 1}`
- If no such `j` exists, the answer is `0`

**Why subtract 1?** Because position `j` is counted in both `INC[j]` and `DEC[j]`, so we count it once.

## Your Task

Complete the `unimodal.py` file by filling in the critical lines marked with `# your code goes here`.

**Note:** The template uses `pass` statements as placeholders to avoid syntax errors. You should delete `pass` and write your own code in its place.

You need to implement:
1. The recurrence for computing `INC[j]`
2. The recurrence for computing `DEC[j]`
3. The logic to find the maximum unimodal length

## Input/Output Format

### Input Format
Your program must read from standard input (stdin) a single line containing a space-separated list of integers in the following **exact format**:

```
n1 n2 n3 n4 ... nk
```

Where each `ni` is an integer (can be positive, negative, or zero).

**Example Input:**
```
1 5 3 6 4 8 2
```

### Output Format
Your program must output to standard output (stdout) a single integer representing the length of the longest unimodal subsequence in the following **exact format**:

```
length
```

If no valid unimodal subsequence exists (no element can serve as a peak with both increasing and decreasing parts), output `0`.

**Example Output for the input above:**
```
5
```

The longest unimodal subsequence is `[1, 5, 6, 8, 2]` or `[1, 3, 6, 8, 2]` with length 5.

## Additional Test Cases

### Test Case 1: Valid unimodal
**Input:**
```
1 5 3 6 4 8 2
```
**Output:**
```
5
```
**Explanation:** Unimodal: `[1, 5, 6, 8, 2]` or `[1, 3, 6, 8, 2]`

### Test Case 2: Only increasing
**Input:**
```
1 2 3 4 5
```
**Output:**
```
0
```
**Explanation:** No decreasing part, so no valid unimodal subsequence.

### Test Case 3: Only decreasing
**Input:**
```
5 4 3 2 1
```
**Output:**
```
0
```
**Explanation:** No increasing part, so no valid unimodal subsequence.

### Test Case 4: Simple mountain
**Input:**
```
1 3 2
```
**Output:**
```
3
```
**Explanation:** The entire sequence is unimodal: `[1, 3, 2]`.

### Test Case 5: Complex sequence
**Input:**
```
10 9 2 5 3 7 101 18
```
**Output:**
```
5
```
**Explanation:** Unimodal: `[2, 5, 7, 101, 18]` (length 5).

### Test Case 6: Single element
**Input:**
```
5
```
**Output:**
```
0
```
**Explanation:** A single element cannot form a unimodal subsequence (need at least 3 elements).

### Test Case 7: All equal
**Input:**
```
3 3 3 3
```
**Output:**
```
0
```
**Explanation:** No strictly increasing or decreasing parts possible.

## Testing Your Solution

Run your completed file with sample input:

```bash
echo "1 5 3 6 4 8 2" | python3 unimodal.py
```

Expected output:
```
5
```

Test edge cases:

```bash
echo "1 2 3 4 5" | python3 unimodal.py  # Only increasing
```
Expected output: `0`

```bash
echo "1 3 2" | python3 unimodal.py  # Simple mountain
```
Expected output: `3`

## Algorithm Complexity

The dynamic programming solution has:
- **Time Complexity:** O(n²), where n is the number of elements
- **Space Complexity:** O(n) for the two arrays INC and DEC

## Submission

Submit your completed `unimodal.py` file. The auto-grader will test your solution by running the file and checking the output.

# Submitting Assignments with GitHub Classroom

Assignments will be distributed and submitted using GitHub Classroom. Each assignment will be autograded using input/output test cases.

**How to submit:**
1. Accept the assignment link provided by your instructor. This will create a private repository for you.
2. Clone your repository to your computer.
3. Complete your assignment by editing the required files.
4. Make sure your code produces the correct output for the given input (as specified in the assignment).
5. Commit your changes and push them to GitHub.
6. Your submission will be automatically graded based on input/output test cases.

**Tips:**
- Only modify the files specified in the instructions.
- Do not change the filenames or folder structure.
- Test your code locally before pushing.
- You can push multiple times before the deadline; only your latest commit will be graded.

**Working in GitHub Codespaces:**
You can use GitHub Codespaces ("spaces") to work on your assignment directly in your browser. This provides a cloud-based development environment without needing to install anything locally.