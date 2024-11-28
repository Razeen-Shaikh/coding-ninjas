def canYouMakeDifference(n: int, s: str) -> int:
    # Write your code here.
    freq = [0] * 26

    for i in range(n):
        freq[ord(s[i]) - ord('a')] += 1

    unique_count = 0
    for i in range(26):
        if freq[i] > 0:
            unique_count += 1

    if unique_count == 1:
        return 0
    else: return 1