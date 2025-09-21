/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* ptr1 = head;
        ListNode* ptr2 = head->next;
        while (ptr2){
            int temp = ptr1->val;
            ptr1->val = ptr2->val;
            ptr2->val = temp;
            if (ptr2->next == NULL) break;
            ptr1 = ptr1->next->next;
            ptr2 = ptr2->next->next;
        }
        return head;
    }
};