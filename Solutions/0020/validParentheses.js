/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let stack = [];
  let opening = { "{": 1, "(": 2, "[": 3 };
  let closing = { "}": 1, ")": 2, "]": 3 };

  for (letter of s) {
    if (opening[letter] === undefined) {
      if (opening[stack[stack.length - 1]] != closing[letter]) {
        return false;
      } else {
        stack.pop();
      }
    } else {
      stack.push(letter);
    }
  }

  if (stack[0] === undefined) {
    return true;
  } else {
    return false;
  }
};
