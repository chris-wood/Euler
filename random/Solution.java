class Solution {
    public int solution(int X, int[] A) {
        int head = 0;
        int headCount = 0;
        int tail = A.length - 1;
        int tailCount = 0;
        
        while (head < tail) {
            if (A[head] == X) { 
                headCount++;   
            }
            if (A[tail] != X) {
                tailCount++;   
            }
            
            head++;
            tail--;
        }
        
        if (head == tail) {
            if (A[head] == X && headCount + 1 == tailCount) {
                return head + 1;   
            } else if (A[head] == X && headCount == tailCount) {
                return head;
            } else if (A[head] != X && headCount == tailCount + 1) {
                return head;
            } else if (A[head] != X && headCount == tailCount) {
                return head + 1;
            } else {
                return -1;
            }
        } else if (headCount == tailCount) {
            return head;
        } else {
            return -1;
        }
    }
}
