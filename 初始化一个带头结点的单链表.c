typedef struct LNode    //定义单链表结点类型
{                       //每个节点存放一个数据元素
    ElemType data;      //指针指向下一个节点
    struct LNode *next;
}LNode, *LinkList;
bool InitList(LinkList &L)
{
    L = (LNode *) malloc(sizeof(LNode));  //分配一个头结点
    if(L==Null)
        return false;
    L->next=Null;
    return true;
}
void test()
{
    LinkList L;//声明一个指向单链表的指针
    InitList(L);//初始化一个空表
}
