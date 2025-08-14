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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == NULL){
            return list2;
        }
        else if (list2 == NULL){
            return list1;
        }
        
        ListNode* next1 = list1;
        ListNode* next2 = list2;
        ListNode* head;
        if (list1->val > list2->val){
            head = list2;
            next2 = next2->next;
        }
        else {
            head = list1;
            next1 = next1->next;
        }
        ListNode* next = head;
        while (next1 != NULL && next2 != NULL){
            if (next1->val < next2->val){
                next->next = next1;
                next = next->next;
                next1 = next1->next;
            }
            else{
                next->next = next2;
                next = next->next;
                next2 = next2->next;
            }
        }
        if (next1 == NULL){
            next->next = next2;
        }
        else{
            next->next = next1;
        }

        return head;
    }
};