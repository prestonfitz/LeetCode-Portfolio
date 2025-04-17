/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  let negative = false;
  let array = x.toString().split("");
  if (array[0] == "-") {
    negative = true;
    array.shift();
  }
  array.reverse();
  if (negative) {
    array.unshift("-");
  }
  let result = parseInt(array.join(""));
  if (result > 2147483647 || result < -2147483648) {
    return 0;
  } else {
    return result;
  }
};
