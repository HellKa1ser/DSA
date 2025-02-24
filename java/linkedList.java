
public class linkedList {
    public static class Node {
        int data;
        Node next;

        public Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    public static class SLinkedList {
        Node head;

        SLinkedList() {
            this.head = null;
        }

        private void insert_at_beginning(int data) {
            Node newNode = new Node(data);
            newNode.next = head;
            head = newNode;
        }

        private String printLinkedList() {
            Node curr = head;
            StringBuilder sb = new StringBuilder();
            while (curr != null) {
                sb.append(curr.data + " ->");
                curr = curr.next;
            }
            return sb.toString();
        }

        private void reverse_LinkedList() {
            Node prev = null;
            Node curr = head;
            Node next = null;
            while (curr != null) {
                next = curr.next;
                curr.next = prev;
                prev = curr;
                curr = next;
            }
            head = prev;
        }

        private int length() {
            int length = 0;
            Node curr = head;
            while (curr != null) {
                length += 1;
                curr = curr.next;
            }
            return length;
        }

        private void insert_at_end(int data) {
            Node curr = head;
            Node new_node = new Node(data);
            if (head == null) {
                insert_at_beginning(data);
            }
            while (curr.next != null) {
                curr = curr.next;
            }
            curr.next = new_node;
        }

        private void insert_at_pos(int data, int pos) {
            Node curr = head;
            Node new_node = new Node(data);
            if (pos == 0) {
                insert_at_beginning(data);
                return;
            }
            int count = 0;
            while (curr != null && count < pos - 1) {
                curr = curr.next;
                count += 1;
            }
            if (curr == null) {
                System.out.println("The position is out of length");
                insert_at_end(data);
            } else {
                new_node.next = curr.next;
                curr.next = new_node;
            }

        }

        public static SLinkedList mergeLinkedList(SLinkedList sLinkedList1, SLinkedList sLinkedList2) {
            SLinkedList result = new SLinkedList();
            Node head1 = list1.head;
            Node head2 = list2.head;
            while (list1.next != null && list2.next != null) {
                if (head2.data >= head1.data) {
                    result.next = head1;
                    head1 = head1.next;
                } else {
                    result.next = head2;
                    head2 = head2.next;
                }
                result = result.next;
            }
            return result;

        }
    }

    public static void main(String[] args) {
        SLinkedList list1 = new SLinkedList();
        SLinkedList list2 = new SLinkedList();
        list1.insert_at_beginning(1);
        list1.insert_at_end(2);
        list1.insert_at_end(4);
        list1.insert_at_end(6);
        list2.insert_at_beginning(1);
        list2.insert_at_end(3);
        list2.insert_at_end(6);
        list2.insert_at_end(9);
        SLinkedList result = mergeLinkedList(list1, list2);
        System.out.println(result.printLinkedList());
    }

}
