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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* ptr = head;
        ListNode* nextdiff = head;
        while(nextdiff != NULL){
            nextdiff = nextdiff->next;
            if (nextdiff == NULL || ptr-> val != nextdiff->val){
                ptr->next = nextdiff;
                ptr = ptr->next;
            }
        }
        return head;
    }
};