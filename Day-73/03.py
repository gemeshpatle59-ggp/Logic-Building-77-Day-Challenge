# Compare brute-force subarray sum with prefix-sum approach.

"""
| Feature          | Brute-Force Approach                        | Prefix-Sum Approach                             |
|---               |---                                          |---                                              |
| Method           | Adds elements of each subarray individually | Uses cumulative sums to calculate subarray sums |
| Time Complexity  | O(n²) for all subarray sums                 | O(n) preprocessing + O(1) per query             |
| Space Complexity | O(1) extra space                            | O(n) extra space                                |
| Advantage        | Simple to implement                         | Efficient for multiple sum queries              |
| Disadvantage     | Repeatedly calculates the same sums         | Requires additional memory                      |

"""