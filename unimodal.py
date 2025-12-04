#!/usr/bin/env python3
"""
Longest Unimodal Subsequence - Dynamic Programming

A unimodal subsequence first increases strictly, then decreases strictly,
forming a mountain shape. It must have at least one element in both the
increasing and decreasing parts (minimum length 3).

This solution uses two DP arrays:
- INC[j]: length of longest strictly increasing subsequence ending at j
- DEC[j]: length of longest strictly decreasing subsequence starting at j
"""

def compute_inc(arr):
    """
    Compute INC array: length of longest strictly increasing subsequence
    ending at each position.

    Args:
        arr: List of integers

    Returns:
        List where INC[j] = length of longest strictly increasing
        subsequence ending at position j
    """
    n = len(arr)
    INC = [1] * n  # Initialize all positions to 1

    for j in range(1, n):
        # Find the maximum INC[i] where i < j and arr[i] < arr[j]
        max_val = 0
        for i in range(j):
            if arr[i] < arr[j]:
                max_val = max(max_val, INC[i])
        INC[j] = 1 + max_val
    return INC


def compute_dec(arr):
    """
    Compute DEC array: length of longest strictly decreasing subsequence
    starting at each position.

    Args:
        arr: List of integers

    Returns:
        List where DEC[j] = length of longest strictly decreasing
        subsequence starting at position j
    """
    n = len(arr)
    DEC = [1] * n  # Initialize all positions to 1

    for j in range(n - 2, -1, -1):  # Process from right to left
        # Find the maximum DEC[i] where i > j and arr[j] > arr[i]
        max_val = 0
        for i in range(j + 1, n):
            if arr[j] > arr[i]:
                max_val = max(max_val, DEC[i])
        DEC[j] = 1 + max_val
    return DEC


def find_longest_unimodal(arr):
    """
    Find the length of the longest unimodal subsequence.

    Args:
        arr: List of integers

    Returns:
        Integer representing the length of the longest unimodal subsequence,
        or 0 if no valid unimodal subsequence exists
    """
    if len(arr) < 3:
        return 0

    INC = compute_inc(arr)
    DEC = compute_dec(arr)

    max_length = 0

    # For each position j that could be a peak
    for j in range(len(arr)):
        # A valid peak must have both increasing and decreasing parts
        if INC[j] > 1 and DEC[j] > 1:
            unimodal_len = INC[j] + DEC[j] - 1
            max_length = max(max_length, unimodal_len)
    return max_length


def main():
    """
    Read input from stdin and output the length of the longest
    unimodal subsequence.
    """
    # Read input
    line = input().strip()
    arr = list(map(int, line.split()))

    # Compute result
    result = find_longest_unimodal(arr)

    # Output result
    print(result)


if __name__ == "__main__":
    main()
