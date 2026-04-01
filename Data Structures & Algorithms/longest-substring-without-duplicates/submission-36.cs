public class Solution {
    public int LengthOfLongestSubstring(string s) {

        var sols = new Dictionary <int, string>();

        Console.WriteLine($"String is: {s}");
        if (s.Length == 0) return 0;
        if (s.Length == 1) return 1;

        int L = 0;
        int R = 1;
        string currStr = s[L].ToString();

        while (R < s.Length)
        {
            char rChar = s[R];
            Console.WriteLine($"Current substring: {currStr}");

            if (currStr.Contains(rChar))
            {
                Console.WriteLine($"Current substring contains: {rChar} and is {currStr.Length} long");
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

                Console.WriteLine($"Current indexes are L: {L} and R: {R}....continuing");
                continue;
            }

            currStr = s.Substring(L, (R - L) + 1);
            Console.WriteLine($"Increasing substring length: {currStr}");
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

        // if (sols.Count() == 0)
        // {
        //     return s.Length;
        // }

        Console.WriteLine($"Exited loop - dict contains: {sols.Count()} {sols}");
        var sortedSols = sols.OrderByDescending(x => x.Key);

        foreach (var item in sortedSols)
        {
            Console.WriteLine($"Returning: {item.Key}");
            return item.Key;
        }

        Console.WriteLine($"Error - returning 0 for string {s}");

        return 0;
    }
}
