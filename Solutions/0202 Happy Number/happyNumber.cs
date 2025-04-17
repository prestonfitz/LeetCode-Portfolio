public class Solution {
    public bool IsHappy(int n, Dictionary<int, bool> memo = null) {
        if (memo == null) {
            memo = new Dictionary<int, bool>();
        }

        string strN = n.ToString();
        int sum = 0;
        foreach (char digit in strN) {
            sum += (int)Math.Pow(int.Parse(digit.ToString()), 2);
        }

        if (sum == 1) {
            return true;
        } else if (memo.ContainsKey(sum)) {
            return false;
        } else {
            memo[sum] = true;
            return IsHappy(sum, memo);
        }
    }
}