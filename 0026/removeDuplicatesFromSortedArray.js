/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let beg = 0;
  while (beg < nums.length - 1) {
    if (nums[beg] === nums[beg + 1]) {
      nums.splice(beg, 1);
      beg--;
    }
    beg++;
  }

  return nums.length;
};
