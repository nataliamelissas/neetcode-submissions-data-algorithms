public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        // loop through each word
        // order each word alphabetically
        // store that as a dictionary key
        // store an array as the dictionary value with the original word
        
        // after the loop, make an array out of all the values (the arrays)

        // cons: space complexity is double
        
        Dictionary<string, List<string>> strDict = new();
        foreach (string str in strs)
        {
            char[] orderedChars = str.ToCharArray();
            Array.Sort(orderedChars);
            string orderedStr = new string(orderedChars);
        
            if (!strDict.ContainsKey(orderedStr))
            {
                strDict[orderedStr] = new List<string>();
            }
            strDict[orderedStr].Add(str);
        }
        
        return strDict.Values.ToList();
    }
}
