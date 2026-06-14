class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if (len(s) == 1):
            return 1

        count = {}
        maxf = 0
        l, r = 0, 0
        max_len = 0
        # AAAAABABBSDFFFFFEOKDFFAAAAAA k = 3
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            # print (f"maxf: {maxf} and count of letter at right: {count[s[r]]}")

            # if the number of characters in the window that aren't the most frequent is > k
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
                # print (f"count of letter on left: {count[s[l]]} index l: {l}")
            
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len

        