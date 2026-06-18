class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        letters = {}

        for i in range(len(s)):
            # add letter count for s
            counts = letters.setdefault(s[i], [0,0])
            counts[0] = counts[0] + 1 # counts[0] is always for s
            letters[s[i]] = counts

            # add letter count for t
            counts = letters.setdefault(t[i], [0,0])
            counts[1] = counts[1] + 1 # counts[1] is always for t
            letters[t[i]] = counts

        for letter, counts in letters.items():
            print(letter, counts)
            if counts[0] != counts[1]:
                return False

        return True
