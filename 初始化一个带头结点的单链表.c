typedef struct LNode    //���嵥����������
{                       //ÿ���ڵ���һ������Ԫ��
    ElemType data;      //ָ��ָ����һ���ڵ�
    struct LNode *next;
}LNode, *LinkList;
bool InitList(LinkList &L)
{
    L = (LNode *) malloc(sizeof(LNode));  //����һ��ͷ���
    if(L==Null)
        return false;
    L->next=Null;
    return true;
}
void test()
{
    LinkList L;//����һ��ָ�������ָ��
    InitList(L);//��ʼ��һ���ձ�
}
