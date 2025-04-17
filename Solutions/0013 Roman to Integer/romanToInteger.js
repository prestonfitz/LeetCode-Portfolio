/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  let symbols = { I: 0, V: 1, X: 2, L: 3, C: 4, D: 5, M: 6 };
  let numbers = [1, 5, 10, 50, 100, 500, 1000];
  let lastIndex = 0;
  let charArray = s.split("");
  let returnNum = 0;

  while (charArray[0] != undefined) {
    let currentIndex = symbols[charArray[charArray.length - 1]];

    if (currentIndex < lastIndex) {
      returnNum -= numbers[currentIndex];
      charArray.pop();
    } else {
      returnNum += numbers[currentIndex];
      lastIndex = currentIndex;
      charArray.pop();
    }
  }

  return returnNum;
};
