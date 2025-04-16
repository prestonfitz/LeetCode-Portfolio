/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  let counter = {};
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in counter) {
      counter[nums[i]] = counter[nums[i]] + 1;
    } else {
      counter[nums[i]] = 1;
    }
  }

  let maxVal = 0;
  let maxCount = 0;

  for (const [key, value] of Object.entries(counter)) {
    if (value > maxCount) {
      maxVal = key;
      maxCount = value;
    }
  }

  return Number(maxVal);
};
