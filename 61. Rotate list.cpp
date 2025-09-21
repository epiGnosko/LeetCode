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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next) return head;
        ListNode* runner = head;
        int size = 0;
        while (runner){
            runner = runner->next;
            size++;
        }
        k %= size;
        if (!k) return head;
        ListNode* ptr = head;
        ListNode* next = head->next;
        while(next->next){
            ptr = ptr->next;
            next = next->next;
        }
        next->next = head;
        ptr->next = NULL;
        return rotateRight(next, k - 1);
    }
};