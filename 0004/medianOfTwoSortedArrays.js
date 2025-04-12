/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  combinedArray = nums1.concat(nums2);
  combinedArray = combinedArray.sort((a, b) => a - b);
  // console.log(combinedArray)
  let output = 0;

  if (combinedArray.length % 2 == 0) {
    output =
      (combinedArray[combinedArray.length / 2] +
        combinedArray[combinedArray.length / 2 - 1]) /
      2;
    // console.log('even')
  } else {
    output = combinedArray[Math.floor(combinedArray.length / 2)];
    // console.log('odd')
  }

  return output;
};
