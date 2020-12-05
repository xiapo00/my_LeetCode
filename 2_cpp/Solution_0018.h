ListNode* removeNthFromEnd(ListNode* head, int n) {
    int l = 0;
    ListNode* needle = head;
    while (needle) {
        needle = needle->next;
        l++;
    }
    if (l==n) return head->next;
    needle = head;
    for(int i=0; i<l-n-1; i++) needle = needle->next;
    needle->next = needle->next->next;
    return head;
}

void test_0018() {
    ListNode* head = num2List(54321);
    cout << list2Num(removeNthFromEnd(head, 2)) << endl; // 5321
}