/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  let targetDig = digits.length - 1;
  let inProgress = true;

  while (inProgress) {
    if (targetDig >= 0) {
      newNum = digits[targetDig] + 1;

      if (newNum == 10) {
        digits[targetDig] = 0;
        targetDig--;
      } else {
        digits[targetDig] = newNum;
        inProgress = false;
      }
    } else {
      digits.unshift(1);
      inProgress = false;
    }
  }

  return digits;
};
