public class Solution {
    public string IntToRoman(int num) {
        if ((num - 1000) >= 0)
        {
            return "M" + IntToRoman(num - 1000);
        }
        else if ((num - 900) >= 0)
        {
            return "CM" + IntToRoman(num - 900);
        }
        else if ((num - 500) >= 0)
        {
            return "D" + IntToRoman(num - 500);
        }
        else if ((num - 400) >= 0)
        {
            return "CD" + IntToRoman(num - 400);
        }
        else if ((num - 100) >= 0)
        {
            return "C" + IntToRoman(num - 100);
        }
        else if ((num - 90) >= 0)
        {
            return "XC" + IntToRoman(num - 90);
        }
        else if ((num - 50) >= 0)
        {
            return "L" + IntToRoman(num - 50);
        }
        else if ((num - 40) >= 0)
        {
            return "XL" + IntToRoman(num - 40);
        }
        else if ((num - 10) >= 0)
        {
            return "X" + IntToRoman(num - 10);
        }
        else if ((num - 9) >= 0)
        {
            return "IX" + IntToRoman(num - 9);
        }
        else if ((num - 5) >= 0)
        {
            return "V" + IntToRoman(num - 5);
        }
        else if ((num - 4) >= 0)
        {
            return "IV" + IntToRoman(num - 4);
        }
        else if ((num - 1) >= 0)
        {
            return "I" + IntToRoman(num - 1);
        }
        else
        {
            return "";
        }
    }
}
