struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* num2List(int num) {
    ListNode *head = new ListNode(num % 10);
    ListNode *needle = head;
    while(num /= 10) {
        needle->next = new ListNode(num % 10);
        needle = needle->next;
    }
    return head;
}

int list2Num(ListNode* head) {
    int s=0;
    int co=1;
    while(head) {
        s += head->val * co;
        co *= 10;
        head = head->next;
    }
    return s;
}

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    int flag = 0, n1, n2;
    ListNode *head = new ListNode();
    ListNode *needle = head;
    while(l1 || l2) {
        if(l1) n1 = l1->val;
        else n1 = 0;
        if(l2) n2 = l2->val;
        else n2 = 0;
        needle->val = (n1 + n2 + flag) % 10;
        flag = (n1 + n2 + flag >= 10);
        if(flag || (l1 && l1->next) || (l2 && l2->next)) needle->next = new ListNode(1);
        needle = needle->next;
        if(l1 && l1->next) l1 = l1->next;
        else l1 = nullptr;
        if(l2 && l2->next) l2 = l2->next;
        else l2 = nullptr;
    }
    return head;
}

void test_0002()
{
    ListNode *l1, *l2, *r;
    l1 = num2List(342);
    l2 = num2List(465);
    r = addTwoNumbers(l1, l2);
    std::cout << list2Num(r) << std::endl; // 807

    l1 = num2List(999);
    l2 = num2List(999);
    r = addTwoNumbers(l1, l2);
    std::cout << list2Num(r) << std::endl; // 1998

    l1 = num2List(9);
    l2 = num2List(9);
    r = addTwoNumbers(l1, l2);
    std::cout << list2Num(r) << std::endl; // 18

    l1 = num2List(65);
    l2 = num2List(945);
    r = addTwoNumbers(l1, l2);
    std::cout << list2Num(r) << std::endl; // 1010
}