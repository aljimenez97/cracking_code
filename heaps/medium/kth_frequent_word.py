# https://leetcode.com/problems/top-k-frequent-words/submissions/

# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with 
# the same frequency by their lexicographical order.

from collections import Counter
import heapq

def get_kth_frequent_words(words, k):
    counts = Counter(words)
    max_heap = []

    heapq.heapify(max_heap)

    for key, val in counts.items():
        heapq.heappush(max_heap, (-val, key))

    out = [heapq.heappop(max_heap) [1] for _ in range(k)]

    return out

if __name__ == "__main__":
    words = ["i","love","leetcode","i","love","coding"]
    k = 3
    print(get_kth_frequent_words(words, k))



