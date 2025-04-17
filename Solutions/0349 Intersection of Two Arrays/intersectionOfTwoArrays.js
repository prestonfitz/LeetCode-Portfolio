/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
  let result = [];
  let test = {};

  for (i = 0; i < nums1.length; i++) {
    if (nums1[i] in test) {
    } else {
      test[nums1[i]] = 1;
    }
  }

  for (i = 0; i < nums2.length; i++) {
    if (nums2[i] in test) {
      if (test[nums2[i]] == 1) {
        result.push(nums2[i]);
        test[nums2[i]] = 2;
      }
    }
  }

  return result;
};
