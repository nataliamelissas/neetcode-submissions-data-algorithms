public class Solution {
    public int LengthOfLongestSubstring(string s) {

        var sols = new Dictionary <int, string>();

        if (s.Length == 0) return 0;
        if (s.Length == 1) return 1;

        int L = 0;
        int R = 1;
        string currStr = s[L].ToString();

        while (R < s.Length)
        {
            char rChar = s[R];
            if (currStr.Contains(rChar))
            {
                try {
                    sols.Add(currStr.Length, currStr);
                }
                catch (Exception e)
                {
                    Console.WriteLine("Already exists");
                }

                L++;
                currStr = s[L].ToString(); // reset
                R = L + 1;
                continue;
            }

            currStr = s.Substring(L, (R - L) + 1);
            R++;
            
            if (R == s.Length)
            {
                try {
                    sols.Add(currStr.Length, currStr);
                }
                catch (Exception e)
                {
                    Console.WriteLine($"Key {currStr.Length} already exists");
                }
            }
        }
        var sortedSols = sols.OrderByDescending(x => x.Key);
        foreach (var item in sortedSols)
        {
            return item.Key;
        }
        return 0;
    }
}
