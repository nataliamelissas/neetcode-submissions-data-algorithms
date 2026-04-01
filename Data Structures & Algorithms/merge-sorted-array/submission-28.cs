public class Solution {

    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int nums1Idx = m;

        for (int i = 0; i < n; i++)
        {
            nums1[nums1Idx] = nums2[i];
            nums1Idx++;
        }

        Array.Sort(nums1);
    }

    // public void Merge(int[] nums1, int m, int[] nums2, int n) {
        
    //     // Dictionary<int, int> orderedNewValues = {};

    //     if (n <= 0)
    //     {
    //         return;
    //     }

    //     int nums2Idx = 0;
    //     for (int i = 0; i < (m+n); i++)
    //     {
    //         int currValue = nums1[i];
    //         int nums2Value = nums2[nums2Idx];

    //         if (currValue <= nums2Value && m != 0)
    //         {
    //             if (currValue != 0 || i < m)
    //             {
    //                 // Console.WriteLine($"Merge: {currValue}, {nums2Value}");
    //                 continue;
    //             }
    //         }

    //         // Console.WriteLine($"Merge: About to insert new value {nums2Value} to index {i} because it's less than {currValue}");
    //         BubbleUp(nums2Value, i, nums1);

    //         if (nums2Idx == n -1)
    //         {
    //             break;
    //         }

    //         nums2Idx++;
    //     }

    // }

    // private void BubbleUp(int newValue, int newIndex, int[] nums1)
    // {
    //     int currValue = nums1[newIndex];
    //     nums1[newIndex] = newValue;

    //     // Console.WriteLine($"BubbleUp: curr value {currValue} replaced with new value {newValue}");

    //     for (int i = newIndex + 1; i < nums1.Count(); i++)
    //     {
    //         int nextValue = nums1[i];

    //         // Console.WriteLine($"BubbleUp: next value is {nextValue} at index {i}");

    //         nums1[i] = currValue;

    //         // Console.WriteLine($"BubbleUp: bubbled up {currValue} to index {i}");

    //         currValue = nextValue;

    //         // Console.WriteLine($"BubbleUp: new curr value is {currValue}");
    //     }
    // }
}