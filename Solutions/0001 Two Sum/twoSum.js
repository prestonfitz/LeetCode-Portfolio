/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let pairs = {};

  for (num in nums) {
    compliment = target - nums[num];
    if (pairs[compliment] !== undefined) {
      return [pairs[compliment], parseInt(num)];
    } else {
      pairs[nums[num]] = parseInt(num);
    }
  }
};
