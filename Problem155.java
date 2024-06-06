//155 Min Stack

import java.util.Stack;


class MinStack {
    private Stack<Integer> st;
    private int min;

    public MinStack() {
        this.st = new Stack<>();
        this.min = Integer.MAX_VALUE;
    }

    public void push(int val) {
        if (val <= min) {
            // Push the old minimum value
            st.push(min);
            // Update the minimum value
            min = val;
        }
        // Push the actual value
        st.push(val);
        // System.out.println("Stack after push: " + st);
    }

    public void pop() {
        if (st.pop() == min) {
            // If the popped value is the current minimum, pop again to get the old minimum value
            min = st.pop();
        }
        // System.out.println("Stack after pop: " + st);
    }

    public int top() {
        return st.peek();
    }

    public int getMin() {
        return min;
    }
}