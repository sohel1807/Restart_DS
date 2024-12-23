class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

def createlist():
    head=None
    tail=None
    while True:
        user_input=input("Enter a value:").strip()
        if user_input.lower()=="done":
            break

        new_node=ListNode(user_input)
         
    return head

def printlist(head):
    if not head:
        print("List is empty")
        return
    else:
        current=head
        while current:
            print(current.value,end="->")
            current=current.next

if __name__== "__main__":
    linked_list=createlist()
    printlist(linked_list)