public class Solution {
    public int MajorityElement(int[] nums) {
        var counts = new Dictionary<int, int>();
        var answer = nums[0];

        foreach (int num in nums)
        {
            // check if num exists in counts
            var containsNum = counts.ContainsKey(num);

            // if no, add to counts and continue
            if (!containsNum)
            {
                counts.Add(num, 1);
                continue;
            }

            // if yes, add 1 to the value
            counts[num] = counts[num] + 1;

            // if value is >= the length of nums return that key
            if (counts[num] > (nums.Length / 2))
            {
                answer = num;
            }
        }

        return answer;
    }
}