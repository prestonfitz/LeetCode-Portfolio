/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  if (!head) {
    return head;
  }
  let prev = [];

  while (head.next !== null) {
    prev.push(head);
    head = head.next;
  }

  for (let i = 0; i < prev.length; i++) {
    if (i === 0) {
      prev[i].next = null;
    } else {
      prev[i].next = prev[i - 1];
    }
  }

  if (prev.length !== 0) {
    head.next = prev[prev.length - 1];
  }

  return head;
};
